"""
URL configuration for Hackathon IT School Olympiad backend.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

def api_root_view(request):
    return JsonResponse({
        'name': 'Hackathon IT School - Viloyat Matematika Olimpiadasi API',
        'version': 'v1',
        'status': 'online',
        'endpoints': {
            'participants_registration': '/api/v1/participants/',
            'event_info': '/api/v1/event-info/',
            'certificates': '/api/v1/certificates/',
            'health_check': '/api/v1/health/',
            'admin_panel': '/admin/',
        }
    })

urlpatterns = [
    path('', api_root_view, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('participants.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

