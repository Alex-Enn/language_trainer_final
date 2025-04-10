from django.apps import AppConfig


class CardsConfig(AppConfig):
    """Класс карточки конфигурации

    Args:
        AppConfig (_type_): _description_
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "cards"
