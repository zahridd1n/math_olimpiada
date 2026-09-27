"""
Django admin configuration for Olympiad management.
Provides organizer-friendly views with search, filter, and CSV export.
"""
import csv
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import mark_safe
from .models import OlympiadEvent, Participant, Certificate, SiteMediaSettings


def export_participants_csv(modeladmin, request, queryset):
    """Export selected participants to CSV."""
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="participants.csv"'
    response.write('\ufeff')  # BOM for Excel UTF-8
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'F.I.Sh.', 'Telefon', 'Tug\'ilgan sana',
        'Maktab', 'Viloyat', 'Tuman/shahar', 'Sinf',
        'O\'qituvchi', 'Ro\'yxatdan o\'tgan vaqti'
    ])
    for p in queryset.select_related('event'):
        writer.writerow([
            p.id, p.full_name, p.phone,
            p.birth_date.strftime('%Y-%m-%d') if p.birth_date else '',
            p.school, p.region, p.district,
            p.class_number, p.teacher_name,
            p.created_at.strftime('%Y-%m-%d %H:%M') if p.created_at else '',
        ])
    return response

export_participants_csv.short_description = "CSV ga eksport qilish"


@admin.register(OlympiadEvent)
class OlympiadEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'event_date', 'registration_open', 'registration_close', 'participant_count']
    list_filter = ['is_active']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    def participant_count(self, obj):
        return obj.participants.count()
    participant_count.short_description = "Qatnashchilar soni"


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'full_name', 'phone', 'school',
        'class_number', 'district', 'region', 'created_at'
    ]
    list_filter = [
        'event', 'class_number', 'region', 'district',
        'school', 'created_at'
    ]
    search_fields = ['full_name', 'phone', 'school', 'teacher_name']
    list_per_page = 50
    date_hierarchy = 'created_at'
    actions = [export_participants_csv]
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ("Shaxsiy ma'lumotlar", {
            'fields': ('event', 'full_name', 'phone', 'birth_date')
        }),
        ("Ta'lim ma'lumotlari", {
            'fields': ('school', 'region', 'district', 'class_number', 'teacher_name')
        }),
        ("Tizim", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview', 'title', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    readonly_fields = ['image_preview_large', 'created_at']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="height: 50px; width: 70px; object-fit: cover; border-radius: 4px;" />')
        return "Rasm yo'q"
    image_preview.short_description = "Ko'rinishi"

    def image_preview_large(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 250px; max-width: 400px; object-fit: contain; border-radius: 8px;" />')
        return "Rasm yo'q"
    image_preview_large.short_description = "Rasm ko'rinishi"


@admin.register(SiteMediaSettings)
class SiteMediaSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'logo_preview', 'hero_preview', 'school_preview', 'updated_at']
    readonly_fields = ['logo_preview_large', 'hero_preview_large', 'school_preview_large', 'updated_at']

    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="height: 36px; object-fit: contain;" />')
        return "Standart logo"
    logo_preview.short_description = "Logotip"

    def hero_preview(self, obj):
        if obj.hero_image:
            return mark_safe(f'<img src="{obj.hero_image.url}" style="height: 40px; width: 60px; object-fit: cover; border-radius: 4px;" />')
        return "Standart rasm"
    hero_preview.short_description = "Hero rasmi"

    def school_preview(self, obj):
        if obj.school_image:
            return mark_safe(f'<img src="{obj.school_image.url}" style="height: 40px; width: 60px; object-fit: cover; border-radius: 4px;" />')
        return "Standart rasm"
    school_preview.short_description = "Maktab rasmi"

    def logo_preview_large(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="max-height: 100px; object-fit: contain;" />')
        return "Standart logotip ishlatilmoqda"
    logo_preview_large.short_description = "Hozirgi Logotip"

    def hero_preview_large(self, obj):
        if obj.hero_image:
            return mark_safe(f'<img src="{obj.hero_image.url}" style="max-height: 200px; border-radius: 8px; object-fit: cover;" />')
        return "Standart Hero rasmi ishlatilmoqda"
    hero_preview_large.short_description = "Hozirgi Hero rasmi"

    def school_preview_large(self, obj):
        if obj.school_image:
            return mark_safe(f'<img src="{obj.school_image.url}" style="max-height: 200px; border-radius: 8px; object-fit: cover;" />')
        return "Standart Maktab rasmi ishlatilmoqda"
    school_preview_large.short_description = "Hozirgi Maktab rasmi"

    def has_add_permission(self, request):
        # Only allow 1 instance
        if SiteMediaSettings.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


