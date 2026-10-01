"""
Django admin configuration for Olympiad management.
Provides organizer-friendly views with search, filter, and CSV export.
"""
import csv
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import mark_safe
from .models import OlympiadEvent, Participant, Certificate, SiteMediaSettings


import io
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def export_participants_excel(modeladmin, request, queryset):
    """Export selected participants to Excel (.xlsx)."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Qatnashchilar"

    header_fill = PatternFill(start_color="1A2035", end_color="1A2035", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    header_alignment = Alignment(horizontal="center", vertical="center")

    thin_border = Border(
        left=Side(style='thin', color='D3D3D3'),
        right=Side(style='thin', color='D3D3D3'),
        top=Side(style='thin', color='D3D3D3'),
        bottom=Side(style='thin', color='D3D3D3')
    )

    headers = ['ID', 'F.I.SH.', 'Telefon', 'Sinf', 'Ro\'yxatdan o\'tgan vaqti']
    ws.append(headers)
    ws.row_dimensions[1].height = 25

    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = header_alignment
        cell.border = thin_border

    row_font = Font(name="Calibri", size=10)
    for row_idx, p in enumerate(queryset.select_related('event'), start=2):
        created_str = p.created_at.strftime('%Y-%m-%d %H:%M') if p.created_at else ''
        ws.append([
            p.id,
            p.full_name,
            p.phone,
            f"{p.class_number}-sinf",
            created_str
        ])
        ws.row_dimensions[row_idx].height = 20

        for col_idx in range(1, len(headers) + 1):
            cell = ws.cell(row=row_idx, column=col_idx)
            cell.font = row_font
            cell.border = thin_border
            if row_idx % 2 == 1:
                cell.fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 14)

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    response = HttpResponse(
        output.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="qatnashchilar.xlsx"'
    return response

export_participants_excel.short_description = "Excel (.xlsx) ga eksport qilish"


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
    actions = [export_participants_excel]
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


