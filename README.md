# Проект Foodgram - ваш продуктовый помощник

Пользователи Foodgram могут публиковать свои любимые рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Для удобства навигации по сайту рецепты размечены тэгами.

# Структура проекта
- frontend - файлы, необходимые для сборки фронтенда приложения;
- infra - инфраструктура проекта: конфигурационный файл nginx и docker-compose.yml;
- backend - файлы, необходимые для сборки бэкенд приложения;
- data - подготовлен список ингредиентов с единицами измерения. Экспорт ингредиентов осуществляется командой ```python manage.py loaddata ingredients.json```

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

4. Создайте фаил .env в директории проекта 'infra-local':
```
SECRET_KEY = 'secret key used in production'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
5. В этой же директории выполните команду сборки контейнеров:
```
docker compose up -d
```
6. Выполните миграции, создайте суперпользователя и соберите статику:
```
docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
docker compose exec backend python manage.py collectstatic --no-input
```
Сайт станет доступен для работы:

- Документация API: http://localhost/api/docs/redoc.html
- Панель администратора: http://localhost/admin/
- Главная страница сайта: http://localhost/recipes

7. При необходимости, выполните импорт ингредиентов:
```
docker compose exec backend python manage.py loaddata ingredients.json
```

## Запуск проекта на сервере (через Docker контейнеры)
VM (Ubuntu 22.04) для Docker Compose V2:

1. Остановите работу nginx, если он у вас установлен и запущен

```
sudo systemctl stop nginx
```

2. Установите последние обновления на виртуальную машину:

```
sudo apt update
sudo apt upgrade -y
```

3. Установите Docker Docker Compose V2

```
sudo apt install docker.io

sudo mkdir -p /usr/local/lib/docker/cli-plugins

sudo curl -SL https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-linux-x86_64 -o /usr/local/lib/docker/cli-plugins/docker-compose

sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
```

## Подготовка сервера для запуска проекта:

- Укажите публичный адрес вашего сервера в nginx.conf
```
server_name <ip вашего сервера>;
```
5. Скопируйте на сервер файлы docker-compose.yml, nginx.conf из папки infra-server (команды выполнять находясь в папке infra-server):
```
scp docker-compose.yml nginx.conf username@IP:/home/username/
```
6. Для работы с GitHub Actions и деплоя необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:
```
SECRET_KEY              # секретный ключ Django проекта
DOCKER_PASSWORD         # пароль от Docker Hub
DOCKER_USERNAME         # логин Docker Hub
HOST                    # публичный IP сервера
USER                    # имя пользователя на сервере
PASSPHRASE              # *если ssh-ключ защищен паролем
SSH_KEY                 # приватный ssh-ключ
TELEGRAM_TO             # ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          # токен бота, посылающего сообщение

DB_ENGINE               # django.db.backends.postgresql
DB_NAME                 # postgres
POSTGRES_USER           # postgres
POSTGRES_PASSWORD       # postgres
DB_HOST                 # db
DB_PORT                 # 5432 (порт по умолчанию)
```

7. После успешного запуска контейнеров выполните
```
docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
docker compose exec backend python manage.py collectstatic --no-input
```

8. Выполните импорт ингредиентов:
```
docker compose exec backend python manage.py loaddata ingredients.json
```

## Github Actions CI:
После каждого обновления репозитория (push в ветку master) будет происходить:
1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
2. Сборка и доставка докер-образов frontend и backend на Docker Hub
3. Разворачивание проекта на удаленном сервере
4. Отправка сообщения в Telegram в случае успеха

Сайт станет доступным для работы (адрес сервера дан для примера):

Документация API: http://158.160.42.251/api/docs/redoc.html
Панель администратора: http://158.160.42.251/admin
Главная страница сайта: http://158.160.42.251/recipes