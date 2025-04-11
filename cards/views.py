"""View-функции для работы с карточками."""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Card
from .forms import CardForm


def home(request):
    """Отображает домашнюю страницу."""
    return render(request, 'cards/home.html')


def add_card(request):
    """
    Обрабатывает добавление новой карточки.
    GET - отображает форму, POST - сохраняет новую карточку.
    """
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm()

    return render(request, 'cards/add_card.html', {'form': form})


def card_list(request):
    """Отображает список всех карточек."""
    cards = Card.objects.all().order_by('-created_at')
    return render(request, 'cards/card_list.html', {'cards': cards})


def practice(request):
    """Отображает страницу для тренировки."""
    cards = Card.objects.all()
    return render(request, 'cards/practice.html', {'cards': cards})

@require_POST
def delete_card(request, card_id):
    """Удаляет карточку по ID."""
    card = get_object_or_404(Card, id=card_id)
    card.delete()
    return redirect('card_list')


def edit_card(request, card_id):
    """
    Редактирует существующую карточку.
    GET - отображает форму, POST - сохраняет изменения.
    """
    card = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm(instance=card)
    return render(request, 'cards/edit_card.html', {'form': form})
