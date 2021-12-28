# Описание проетка:

API для проекта Yatube - социальная сеть


# Запуск:
    Клонировать репозиторий:
        <git clone https://github.com/DevCatRain/api_final_yatube.git>
    
    Перейти в него в командной строке:
        <cd api_yamdb>

    Cоздать и активировать виртуальное окружение:
        <python -m venv venv>
        <source venv/Scripts/activate>
    
    Обновить менеджер пакетов:
        <python -m pip install --upgrade pip>

    Установить зависимости из файла requirements.txt:
        <pip install -r requirements.txt>

    Выполнить миграции:
        <python manage.py migrate>

    Запустить проект:
        <python manage.py runserver>


# Примеры запросов к api:

GET-Response: http://127.0.0.1:8000/api/v1/posts/
Request:

[
    {
        'id': 1,
        'author': 'author',
        'image':''
        'text': 'text',
        'pub_date': 'pub_date',
        'group': null
    },
]


POST-Response: http://127.0.0.1:8000/api/v1/posts/
Поле text обязательное:

{
    'text': 'text'
}

Request:

{
    'id': 5,
    'author': 'admin',
    'image': '',
    'text': 'text',
    'pub_date': 'pub_date',
    'group': null
}


GET-Response: http://127.0.0.1:8000/api/v1/posts/1/comments/
Request:

[
    {
        'id': 1,
        'author': 'author',
        'text': 'text',
        'created': 'created',
        'post': 1
    },
]


POST-Response: http://127.0.0.1:8000/api/v1/follow/
Поле following обязательное:

{
    'following': 'test'
}

Request:

{
    'id': 4,
    'user': 'user',
    'following': 'test'
}
