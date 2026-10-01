"""
URL patterns for the participants API.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('participants/', views.register_participant, name='register-participant'),
    path('participants/<int:pk>/', views.delete_participant, name='delete-participant'),
    path('applications/', views.list_participants, name='list-applications'),
    path('applications/export/', views.export_participants_excel, name='export-applications'),
    path('event-info/', views.event_info, name='event-info'),
    path('certificates/', views.list_certificates, name='list-certificates'),
    path('site-settings/', views.site_media_settings, name='site-media-settings'),
    path('health/', views.health_check, name='health-check'),
]
