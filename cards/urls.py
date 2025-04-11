"""URL-маршруты для приложения cards."""
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    # Работа с карточками
    path('add/', views.add_card, name='add_card'),
    path('cards/', views.card_list, name='card_list'),
    path('practice/', views.practice, name='practice'),
    path('delete/<int:card_id>/', views.delete_card, name='delete_card'),
    # Тренировка
    path('edit/<int:card_id>/', views.edit_card, name='edit_card'),
]
