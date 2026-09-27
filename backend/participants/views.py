"""
API views for participant registration.
"""
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from django.http import JsonResponse

from .models import OlympiadEvent, Participant, Certificate, SiteMediaSettings
from .serializers import (
    ParticipantSerializer,
    EventInfoSerializer,
    CertificateSerializer,
    SiteMediaSettingsSerializer
)


class RegistrationThrottle(AnonRateThrottle):
    """Throttle for registration endpoint — 10 submissions per minute."""
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
        return Response(
            {'error': "Hozirda faol olimpiada mavjud emas."},
            status=status.HTTP_400_BAD_REQUEST
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

