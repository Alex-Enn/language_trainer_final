"""Администрирование карточек в панели администратора."""
from django.contrib import admin
from django.utils.html import format_html
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """Настройки отображения модели Card в админ-панели."""
    list_display = ('word', 'translation', 'created_at', 'image_preview')
    list_filter = ('created_at',)
    search_fields = ('word', 'translation')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'image_preview')
    fieldsets = (
        (None, {
            'fields': ('word', 'translation')
        }),
        ('Медиа', {
            'fields': ('image', 'image_preview'),
            'classes': ('collapse',)
        }),
        ('Дополнительно', {
            'fields': ('created_at',),
            'classes': ('wide',)
        }),
    )
    def image_preview(self, obj):
        """Отображает превью изображения в админке."""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = 'Превью'
