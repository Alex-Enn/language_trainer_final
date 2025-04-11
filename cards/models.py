"""Модели приложения cards."""
from django.db import models

class Card(models.Model):
    """Модель Card для хранения карточек"""
    word = models.CharField(max_length=100, verbose_name="Слово")
    image = models.ImageField(upload_to="cards/images/", verbose_name="Иллюстрация")
    translation = models.CharField(max_length=100, verbose_name="Перевод")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.word  # Для удобного отображения в админке
