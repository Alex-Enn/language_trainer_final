# Language Trainer

Приложение для изучения иностранных языков через практику и повторение.

## Основные возможности

- 📚 Изучение слов и фраз по темам
- 🔁 Система интервального повторения (Spaced Repetition)
- 🎮 Интерактивные упражнения (карточки)

### Планируемые обновления

- 📊 Отслеживание прогресса обучения
- 🎧 Упражнения на аудирование
- 📝 Тестовые задания
- 🔐 Система пользовательских аккаунтов

## Технологии

**Backend**: Django  
**Database**: SQLite  
**Frontend**: HTML, CSS, JavaScript

## Установка

### Предварительные требования

- Python 3.1x
- Установленный pip

### Пошаговая инструкция

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Alex-Enn/language_trainer_final.git
cd language_trainer_final
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
```

3 Установите библиотеки:
```bash
pip install -r requirements.txt
```

4. Настройте SECRET_KEY:
   Откройте файл settings.py и установите свой SECRET_KEY:
```bash
SECRET_KEY = 'ваш_секретный_ключ'
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Запустите сервер:
```bash
python manage.py runserver
```
Приложение будет доступно по адресу: http://localhost:8000

## 🤝 Как внести вклад
Мы приветствуем вклад в проект! Пожалуйста, следуйте этим шагам:

- Форкните репозиторий
- Создайте ветку для вашей фичи ```(git checkout -b feature/AmazingFeature)```
- Сделайте коммит ваших изменений ```(git commit -m 'Add some AmazingFeature')```
- Запушьте в ветку ```(git push origin feature/AmazingFeature)```

Откройте Pull Request

## 📬 Контакты
Автор проекта: Alex-Enn

Email: alex-enn@yandex.ru


## ⭐ Не забудьте поставить звезду, если проект вам понравился!












