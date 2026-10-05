"""
Database models for the Olympiad participant registration system.

Designed to support multiple events in the future while keeping
the first version simple.
"""
from django.db import models
from django.core.validators import RegexValidator


class OlympiadEvent(models.Model):
    """
    Represents a single olympiad event.
    Allows the system to support multiple events over time.
    """
    title = models.CharField(max_length=255, verbose_name="Nomi")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    registration_open = models.DateTimeField(
        null=True, blank=True, verbose_name="Ro'yxatdan o'tish boshlanishi"
    )
    registration_close = models.DateTimeField(
        null=True, blank=True, verbose_name="Ro'yxatdan o'tish tugashi"
    )
    event_date = models.DateField(
        null=True, blank=True, verbose_name="Olimpiada sanasi"
    )
    location = models.CharField(
        max_length=255, blank=True, verbose_name="Manzil"
    )
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Olimpiada"
        verbose_name_plural = "Olimpiadalar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


phone_validator = RegexValidator(
    regex=r'^\+?998\d{9}$',
    message="Telefon raqami to'g'ri formatda bo'lishi kerak: +998XXXXXXXXX"
)


class Participant(models.Model):
    """
    Represents a single participant registration for an olympiad event.
    Duplicate protection is enforced via unique_together on (event, phone).
    """
    CLASS_CHOICES = [(i, f"{i}-sinf") for i in range(5, 8)]

    event = models.ForeignKey(
        OlympiadEvent,
        on_delete=models.CASCADE,
        related_name='participants',
        verbose_name="Olimpiada"
    )
    full_name = models.CharField(max_length=255, verbose_name="F.I.Sh.")
    phone = models.CharField(
        max_length=13,
        validators=[phone_validator],
        verbose_name="Telefon raqami"
    )
    birth_date = models.DateField(null=True, blank=True, verbose_name="Tug'ilgan sana")
    school = models.CharField(max_length=255, blank=True, default="", verbose_name="Maktab nomi")
    region = models.CharField(max_length=100, blank=True, default="", verbose_name="Viloyat")
    district = models.CharField(max_length=100, blank=True, default="", verbose_name="Tuman/shahar")
    class_number = models.PositiveSmallIntegerField(
        choices=CLASS_CHOICES,
        verbose_name="Sinf"
    )
    teacher_name = models.CharField(
        max_length=255, blank=True, default="", verbose_name="O'qituvchi F.I.Sh."
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan vaqti")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Qatnashchi"
        verbose_name_plural = "Qatnashchilar"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['phone']),
            models.Index(fields=['full_name']),
            models.Index(fields=['school']),
            models.Index(fields=['district']),
            models.Index(fields=['class_number']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.full_name} — {self.school} ({self.class_number}-sinf)"


class Certificate(models.Model):
    """
    Olimpiada sertifikatlari va rasmlari galereyasi.
    Django admin orqali yuklanadi va boshqariladi.
    """
    title = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha/Izoh (ixtiyoriy)")
    image = models.ImageField(upload_to="certificates/", verbose_name="Sertifikat / Rasm")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Saytda ko'rsatilsin")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuklangan vaqti")

    class Meta:
        verbose_name = "Sertifikat / Galereya rasmi"
        verbose_name_plural = "Sertifikatlar va Galereya"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title or f"Sertifikat #{self.id}"


class SiteMediaSettings(models.Model):
    """
    Saytning asosiy rasmlari va logotipini boshqarish.
    Django admin orqali yuklanadi.
    """
    site_name = models.CharField(max_length=255, default="Hackathon IT School", verbose_name="Sayt/Maktab nomi")
    logo = models.ImageField(upload_to="site/", blank=True, null=True, verbose_name="Sayt Logotipi (PNG/SVG/JPG)")
    hero_image = models.ImageField(upload_to="site/", blank=True, null=True, verbose_name="Hero (Bosh sahifa) asosiy rasmi")
    school_image = models.ImageField(upload_to="site/", blank=True, null=True, verbose_name="Maktab haqida bo'limi rasmi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Oxirgi tahrirlangan")

    class Meta:
        verbose_name = "Sayt Rasmlari va Logotip"
        verbose_name_plural = "Sayt Rasmlari va Logotip sozlamalari"

    def __str__(self):
        return f"Sayt Rasmlari ({self.site_name})"

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(id=1)
        return obj


