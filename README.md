![Yamdb](https://github.com/da-semenov/yamdb_final/workflows/main/badge.svg)

# API для сервиса YAMDB
## 
**YAMDB**  представляет собой базу отзывов пользователей о фильмах, книгах и музыке.
Проект представляет собой web-приложение и базу данных, поднятых в двух docker-контейнерах.

При разработке приложения использованы фреймфорки ```django и django-rest-framework```. В качестве базы выступает ```postgresql```.
Запуск проекта осуществляется средствами ```docker```.

## Установка

#### 1. Клонируйте репозиторий на локальную машину
```bash
git clone https://github.com/da-semenov/infra_sp2
```

#### 2. В корневой папке необходимо создать файл .env с данными для подключения к базе данных ```postgresql``` по примеру:
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql

DB_NAME=postgres # имя базы данных

POSTGRES_USER=postgres # логин для подключения к базе данных

POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)

DB_HOST=db # название сервиса (контейнера)

DB_PORT=5432 # порт для подключения к БД

#### 3. Установите docker и docker-compose

Если у вас уже установлены docker и docker-compose, этот шаг можно пропустить, иначе можно воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).

#### 4. Запустите процесс сборки и запуска контейнеров
```bash
docker-compose up
```

#### 5. Запустите терминал внутри контейнера
```bash
docker-compose exec web bash
```

#### 6. Выполните миграции
```bash
python manage.py migrate
```

#### 7. Создайте суперпользователя для работы с админкой ```Django```
```bash
python manage.py createsuperuser
```

#### 8. Заполните базу тестовыми данными (по желанию)
```bash
python manage.py loaddata fixtures.json
```

#### 9. Остановить работу можно командой
```bash
docker-compose down
```

## Работа с api
Документация по всем командам описана в redoc

## Основные использованные технологии
* python 3.8
* [django](https://www.djangoproject.com/)
* [drf](https://www.django-rest-framework.org/)
* [posgresql](https://www.postgresql.org/)
* [docker](https://www.docker.com/)
