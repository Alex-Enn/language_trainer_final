"""Формы для работы с карточками."""
from django import forms
from .models import Card


class CardForm(forms.ModelForm):
    """Форма для создания и редактирования карточек.

    Поля:
        word: Текст слова/фразы (обязательное поле)
        image: Изображение для ассоциации (необязательное)
        translation: Перевод слова/фразы (обязательное поле)
    """

    class Meta:
        """Мета-класс для настройки формы."""
        model = Card
        fields = ['word', 'image', 'translation']
        labels = {
            'word': 'Слово',
            'image': 'Иллюстрация',
            'translation': 'Перевод',
        }
        widgets = {
            'word': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите слово или фразу'
            }),
            'translation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите перевод'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
        help_texts = {
            'image': 'Загрузите изображение (необязательно)',
        }

    def clean(self):
        """Валидация формы."""
        cleaned_data = super().clean()
        word = cleaned_data.get('word')
        translation = cleaned_data.get('translation')

        if word and translation and word.lower() == translation.lower():
            raise forms.ValidationError(
                "Слово и перевод не должны быть одинаковыми"
            )

        return cleaned_data
