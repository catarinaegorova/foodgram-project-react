# Проект Foodgram - ваш продуктовый помощник

Пользователи Foodgram могут публиковать свои любимые рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Для удобства навигации по сайту рецепты размечены тэгами.

# Структура проекта
- frontend - файлы, необходимые для сборки фронтенда приложения;
- infra — инфраструктура проекта: конфигурационный файл nginx и docker-compose.yml;
- backend - файлы, необходимые для сборки бэкенд приложения;

# Пользовательские роли 
- Анонимный пользователь
- Аутентифицированный пользователь
- Администратор

### Анонимные пользователи могут:
- Просматривать список рецептов;
- Просматривать отдельные рецепты;
- Фильтровать рецепты по тегам;
- Создавать аккаунт

### Аутентифицированные пользователи могут:
- Получать данные о своей учетной записи;
- Изменять свой пароль;
- Просматривать, публиковать, удалять и редактировать свои рецепты;
- Добавлять понравившиеся рецепты в избранное и удалять из избранного;
- Добавлять рецепты в список покупок и удалять из списка;
- Подписываться и отписываться на авторов;
- Скачивать список покупок

## Описание API

### Ресурсы проекта

- Ресурс `auth`: аутентификация;
- Ресурс `users`: пользователи;
- Ресурс `tags`: теги рецептов ("Завтрак", "Обед", "Ужин");
- Ресурс `recipes`: описание рецептов; 
- Ресурс `ingredients`: ингредиенты, входящие в состав рецептов;

### Документация

В документации указаны эндпоинты (адреса, по которым можно сделать запрос), разрешённые типы запросов, права доступа и дополнительные параметры (паджинация, поиск, фильтрация итд.), когда это необходимо.

### Примеры запросов

- Просмотр списока пользователей
```
GET /api/users/?page=<integer>&limit=<integer>
```
- Регистрация пользователя
```
POST /api/users/
```
- Получение токена авторизации
```
POST /api/auth/token/login/
```
Пример JSON body:
```
{
    "password": "Qwerty123",
    "email": "user@host.ru"
}
```
- Изменение пароля
```
POST /api/users/set_password/
```
- Изменение данных пользователя (своих):
```
POST/PATCH /api/users/me/
```
- Просмотр тегов
```
GET /api/tags/
```
- Просмотр списка рецептов
```
GET /api/recipes/
```
Пример ответа:
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "tags": [
                {
                    "id": 1,
                    "name": "Завтрак",
                    "color": "#49B64E",
                    "slug": "zavtrak"
                }
            ],
            "author": {
                "email": "vpupkin@yandex.ru",
                "id": 3,
                "username": "vasia.pupkin",
                "first_name": "Вася",
                "last_name": "Пупкин",
                "is_subscribed": false
            },
            "ingredients": [
                {
                    "id": 2,
                    "name": "ячмень",
                    "measurement_unit": "г",
                    "amount": 100
                }
            ],
            "is_favorited": false,
            "is_in_shopping_cart": false,
            "name": "Рецепт от Васи",
            "image": "http://127.0.0.1:8000/media/recipes/images/%D0%9A%D0%BE%D0%BD%D0%B4%D0%B8%D1%86%D0%B8%D0%BE%D0%BD%D0%B5%D1%80_%D0%B2_%D0%9C%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE.PNG",
            "text": "Описание рецепта",
            "cooking_time": 10
        }
    ]
}
```
- Создание / Изменение собственного рецепта и удаление рецепта
```
POST/PATCH/DELETE /api/recipes
```
Пример JSON body:
```
{
    "ingredients": [
        {
            "id": 1123,
            "amount": 10
        }
    ],
    "tags": [
        1
    ],
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
    "name": "string",
    "text": "string",
    "cooking_time": 1
}
```
- Добавление в список покупок и удаление из списка
```
POST/DELETE /api/recipes/5/shopping_cart/
```
- Добавление в список избранного и удаление из списка
```
POST/DELETE /api/recipes/5/favorite/
```
- Просмотр списка подписок на авторов
```
GET /api/users/subscriptions/
```
- Просмотр списка подписок на авторов
```
GET /api/users/subscriptions/
```
- Подписка на автора и снятие подписки
```
POST/DELETE /api/users/3/subscribe/ 
```
- Просмотр списка доступных ингредиентов
```
GET /api/ingredients/
```

## Локальный запуск проекта (через Docker контейнеры)
1. Скопируйте репозиторий и перейдите в него в командной строке:

```
git clone git@github.com:catarinaegorova/foodgram-project-react.git
```

```
cd foodgram-project-react
```

2. Создайте и активируйте виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

3. Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Создайте фаил .env в директории проекта 'infra':
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```
5. Примените следующие настройки для 'docker-compose.yml':
```
version: '3.3'
services:
  db:
    image: postgres:14-alpine
    env_file:
      - .env
    ports:
      - 5432:5432 # открываем порты наружу
    volumes:
      - db_data:/var/lib/postgresql/data/
  frontend:
    build:
      context: ../frontend
      dockerfile: Dockerfile
    volumes:
      - ../frontend/:/app/result_build/
  nginx:
    image: nginx:1.19.3
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - ../frontend/build:/usr/share/nginx/html/
      - ../docs/:/usr/share/nginx/html/api/docs/
volumes:
  db_data:
```
6. Примените следующие настройки для 'nginx.conf':
```
server {
    listen 80;
    location /api/ {
        proxy_pass http://host.docker.internal:8000; # эта настройка позволяет обращаться по адресу localhost
    }
    location /admin/ {
        proxy_pass http://host.docker.internal:8000/admin/;
    }
    location /api/docs/ {
        root /usr/share/nginx/html;
        try_files $uri $uri/redoc.html $uri/swagger.html;
    }
    location / {
        root /usr/share/nginx/html;
        index  index.html index.htm;
        try_files $uri /index.html;
        proxy_set_header        Host $host;
        proxy_set_header        X-Real-IP $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header        X-Forwarded-Proto $scheme;
      }
      error_page   500 502 503 504  /50x.html;
      location = /50x.html {
        root   /var/html/frontend/;
      }
}
```
7. Перейдите в папку 'infra-Dev' и выполните команду сборки контейнеров:
```
cd infra-Dev/
```
```
docker compose up
```

Выполните миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
8. Создайте учетную запись администратора:
```
python manage.py createsuperuser
```

9. Загрузите тестовые данные:

```
python manage.py import_ingredients
```

10. Запустите бекэнд сервер:

```
python manage.py runserver
```

11. Откройте вебсайт в браузере и начните работу с сайтом:
```
http://localhost/signin