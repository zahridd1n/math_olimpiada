import csv
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .models import OlympiadEvent, Participant, Certificate, SiteMediaSettings
from .serializers import (
    ParticipantSerializer,
    EventInfoSerializer,
    CertificateSerializer,
    SiteMediaSettingsSerializer
)


class RegistrationThrottle(AnonRateThrottle):
    """Throttle for registration endpoint — 15 submissions per minute."""
    scope = 'participants_registration'


@api_view(['POST'])
@throttle_classes([RegistrationThrottle])
def register_participant(request):
    """
    POST /api/v1/participants/
    Register a new participant for the currently active olympiad event.
    """
    # Find the active event
    event = OlympiadEvent.objects.filter(is_active=True).first()
    if not event:
        # If no event exists yet, create or get a default active event
        event, _ = OlympiadEvent.objects.get_or_create(
            slug='viloyat-matematika-olimpiadasi-2026',
            defaults={
                'title': 'Viloyat matematika olimpiadasi',
                'is_active': True,
                'location': "Farg'ona shahri",
            }
        )

    serializer = ParticipantSerializer(
        data=request.data,
        context={'event': event}
    )

    if serializer.is_valid():
        participant = serializer.save(event=event)
        return Response(
            {
                'id': participant.id,
                'message': "Ro'yxatdan o'tish muvaffaqiyatli yakunlandi",
            },
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_participants(request):
    """
    GET /api/v1/applications/
    Return list of participants for the dashboard with search, filters, and stats.
    """
    queryset = Participant.objects.all().order_by('-created_at')

    search = request.GET.get('search', '').strip()
    if search:
        queryset = queryset.filter(
            Q(full_name__icontains=search) |
            Q(phone__icontains=search)
        )

    class_number = request.GET.get('class_number')
    if class_number and class_number.isdigit():
        queryset = queryset.filter(class_number=int(class_number))

    serializer = ParticipantSerializer(queryset, many=True)

    all_participants = Participant.objects.all()
    stats = {
        'total': all_participants.count(),
        'class_5': all_participants.filter(class_number=5).count(),
        'class_6': all_participants.filter(class_number=6).count(),
        'class_7': all_participants.filter(class_number=7).count(),
        'class_8': all_participants.filter(class_number=8).count(),
    }

    return Response({
        'stats': stats,
        'count': queryset.count(),
        'results': serializer.data
    })


@api_view(['DELETE'])
def delete_participant(request, pk):
    """
    DELETE /api/v1/participants/<pk>/
    Delete a participant registration from dashboard.
    """
    try:
        participant = Participant.objects.get(pk=pk)
        participant.delete()
        return Response({'message': "Muvaffaqiyatli o'chirildi"}, status=status.HTTP_200_OK)
    except Participant.DoesNotExist:
        return Response({'error': "Ishtirokchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def export_participants_excel(request):
    """
    GET /api/v1/applications/export/
    Export participants list to Excel-ready CSV with UTF-8 BOM.
    """
    queryset = Participant.objects.all().order_by('-created_at')

    search = request.GET.get('search', '').strip()
    if search:
        queryset = queryset.filter(
            Q(full_name__icontains=search) |
            Q(phone__icontains=search)
        )

    class_number = request.GET.get('class_number')
    if class_number and class_number.isdigit():
        queryset = queryset.filter(class_number=int(class_number))

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="qabullar_olimpiada.csv"'
    response.write('\ufeff')  # BOM for UTF-8 in Excel
    writer = csv.writer(response)
    writer.writerow(['ID', 'F.I.SH.', 'Telefon', 'Sinf', 'Ro\'yxatdan o\'tgan vaqti'])

    for p in queryset:
        writer.writerow([
            p.id,
            p.full_name,
            p.phone,
            f"{p.class_number}-sinf",
            p.created_at.strftime('%Y-%m-%d %H:%M') if p.created_at else ''
        ])

    return response


@api_view(['GET'])
def event_info(request):
    """
    GET /api/v1/event-info/
    Return public information about the currently active olympiad.
    """
    event = OlympiadEvent.objects.filter(is_active=True).first()
    if not event:
        return Response(
            {'error': "Hozirda faol olimpiada mavjud emas."},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = EventInfoSerializer(event)
    return Response(serializer.data)


@api_view(['GET'])
def list_certificates(request):
    """
    GET /api/v1/certificates/
    Return active certificates / gallery items for the frontend carousel.
    """
    certificates = Certificate.objects.filter(is_active=True).order_by('order', '-created_at')
    serializer = CertificateSerializer(certificates, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def site_media_settings(request):
    """
    GET /api/v1/site-settings/
    Return dynamic logo and site images uploaded from Django admin.
    """
    settings = SiteMediaSettings.get_settings()
    serializer = SiteMediaSettingsSerializer(settings, context={'request': request})
    return Response(serializer.data)


def health_check(request):
    """Simple health check endpoint."""
    return JsonResponse({'status': 'ok'})


