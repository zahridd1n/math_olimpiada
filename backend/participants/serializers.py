"""
DRF serializers for participant registration.
"""
from rest_framework import serializers
from .models import Participant, OlympiadEvent


class ParticipantSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new participant registration.
    The 'event' field is not exposed to the frontend — the view
    automatically assigns the currently active event.
    """

    class Meta:
        model = Participant
        fields = [
            'id',
            'full_name',
            'phone',
            'birth_date',
            'school',
            'region',
            'district',
            'class_number',
            'teacher_name',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'birth_date': {'required': False, 'allow_null': True},
            'school': {'required': False, 'allow_blank': True},
            'region': {'required': False, 'allow_blank': True},
            'district': {'required': False, 'allow_blank': True},
            'teacher_name': {'required': False, 'allow_blank': True},
        }

    def validate_phone(self, value):
        """Normalize phone to +998XXXXXXXXX format."""
        phone = value.strip().replace(' ', '').replace('-', '')
        if not phone.startswith('+'):
            if phone.startswith('998'):
                phone = '+' + phone
            elif phone.startswith('8') and len(phone) == 10:
                phone = '+998' + phone[1:]
            else:
                phone = '+998' + phone
        if len(phone) != 13:
            raise serializers.ValidationError(
                "Telefon raqami to'g'ri formatda bo'lishi kerak: +998XXXXXXXXX"
            )
        return phone

    def validate_class_number(self, value):
        if value < 5 or value > 7:
            raise serializers.ValidationError(
                "Sinf 5 dan 7 gacha bo'lishi kerak."
            )
        return value

    def validate_full_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Ism va familiya kamida 3 ta belgidan iborat bo'lishi kerak."
            )
        return value.strip()


class EventInfoSerializer(serializers.ModelSerializer):
    """Serializer for public event information."""
    participant_count = serializers.SerializerMethodField()

    class Meta:
        model = OlympiadEvent
        fields = [
            'id', 'title', 'slug', 'description',
            'registration_open', 'registration_close',
            'event_date', 'location', 'is_active',
            'participant_count',
        ]

    def get_participant_count(self, obj):
        return obj.participants.count()


class CertificateSerializer(serializers.ModelSerializer):
    """Serializer for certificate gallery images."""
    image_url = serializers.SerializerMethodField()

    class Meta:
        from .models import Certificate
        model = Certificate
        fields = ['id', 'title', 'image', 'image_url', 'order']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return ""


class SiteMediaSettingsSerializer(serializers.ModelSerializer):
    """Serializer for dynamic site logos and images."""
    logo_url = serializers.SerializerMethodField()
    hero_image_url = serializers.SerializerMethodField()
    school_image_url = serializers.SerializerMethodField()

    class Meta:
        from .models import SiteMediaSettings
        model = SiteMediaSettings
        fields = [
            'site_name',
            'logo', 'logo_url',
            'hero_image', 'hero_image_url',
            'school_image', 'school_image_url',
            'updated_at'
        ]

    def _get_absolute_url(self, image_field):
        request = self.context.get('request')
        if image_field and hasattr(image_field, 'url'):
            if request:
                return request.build_absolute_uri(image_field.url)
            return image_field.url
        return ""

    def get_logo_url(self, obj):
        return self._get_absolute_url(obj.logo)

    def get_hero_image_url(self, obj):
        return self._get_absolute_url(obj.hero_image)

    def get_school_image_url(self, obj):
        return self._get_absolute_url(obj.school_image)


