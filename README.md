# SmartRead

Книжный блог с каталогом книг и поиском. Pet project на Django.

## Что уже работает

- Список статей с категориями и тегами
- Детальная страница статьи со счётчиком просмотров
- Похожие статьи на основе общих тегов
- Каталог книг с обложками и авторами
- Поиск по статьям и по книгам
- Админка для управления контентом

## Стек

- Python 3.14, Django 6.1
- PostgreSQL
- Bootstrap 5

## Как запустить локально

1. Клонировать репозиторий: git clone https://github.com/Marina800/SmartRead.git
2. Перейти в папку проекта: cd SmartRead
3. Создать виртуальное окружение: python -m venv venv
4. Активировать виртуальное окружение: venv\Scripts\activate
5. Установить зависимости: pip install django psycopg2-binary python-dotenv Pillow
6. Создать в корне проекта файл .env с такими строками: SECRET_KEY=любой_секретный_ключ, DEBUG=True, DB_NAME=smartread_db, DB_USER=postgres, DB_PASSWORD=ваш_пароль, DB_HOST=127.0.0.1, DB_PORT=5432
7. Создать базу данных в PostgreSQL: CREATE DATABASE smartread_db;
8. Применить миграции: python manage.py migrate
9. Создать администратора: python manage.py createsuperuser
10. Запустить сервер: python manage.py runserver
11. Открыть в браузере: http://127.0.0.1:8000/

## Автор

Марина Гусева — @Marina800


