from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    """_summary_

    Args:
        forms (_type_): _description_
    """
    class Meta:
        """_summary_
        """
        model = Card
        fields = ['word', 'image', 'translation']
        labels = {
            'word': 'Слово',
            'image': 'Иллюстрация',
            'translation': 'Перевод',
        }
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control'}),
        }