![yamdb](https://github.com/da-semenov/yamdb_final/workflows/yamdb/badge.svg?branch=master)

[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646??style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![NGINX](https://img.shields.io/badge/-NGINX-464646??style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![docker](https://img.shields.io/badge/-Docker-464646??style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646??style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

# YaMDB
## 
YAMDB представляет собой базу отзывов пользователей о фильмах, книгах и музыке. Это API, который собирает отзывы пользователей (Review) на произведения (Title). Произведения делятся на категории (Category). В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр (Genres) из списка предустановленных. Новые жанры может создавать только администратор. Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы (Review) и выставляют произведению рейтинг. Сами произведения не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

При разработке приложения использованы фреймфорки ```django и django-rest-framework```. В качестве базы выступает ```postgresql```.
Запуск проекта осуществляется средствами ```docker```. 
Для проекта настроен Continuous Integration и Continuous Deployment:
* автоматический запуск тестов и проверка кода на соответствие стандарту PEP8
* сборка и доставка докер-образов на Docker Hub
* автоматический деплой на боевой сервер при пуше в master после успешного прохождения всех тестов
* отправка уведомления в Telegram о успешном прохождении всех этапов

Для Continuous Integration в проекте используется облачный сервис GitHub Actions. Для него описана последовательность команд (workflow), которая будет выполняться после события push в репозиторий.

## Установка

#### 1. Клонируйте репозиторий на локальную машину
```bash
git clone https://github.com/da-semenov/yamdb_final
```

#### 2. В корневой папке проекта на сервере необходимо создать файл .env с данными для подключения к базе данных ```postgresql```.
В репозитории есть образец .env.example.


#### 3. Добавьте Action secrets в репозитории на GitHub в разделе settings -> Secrets:
* HOST - ip-адрес сервера
* SSH_KEY - приватный ssh ключ
* DOCKER_USERNAME - логин DockerHub
* DOCKER_PASSWORD - пароль DockerHub
* TELEGRAM_TO - id вашего телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
* TELEGRAM_TOKEN - токен бота (получить токен можно у @BotFather, /token, имя бота)


#### 4. После выполнения push необходимо зайти на сервер
```bash
$ ssh username@server_address
```

#### 5. Отобразить список работающих контейнеров
```bash
$ sudo docker container ls
```

#### 6. Зайти в контейнер yamdb по id контейнера
```bash
sudo docker exec -it 1223456789012 bash
```

#### 7. Выполнить миграции внутри этого контейнера
```bash
python manage.py migrate
```

#### 8. Собрать статику
```bash
python manage.py collectstatic
```

#### 9. Создайте суперпользователя для работы с админкой ```Django```
```bash
python manage.py createsuperuser
```

## Работа с api
Документация по всем командам описана в redoc

## Основные использованные технологии
* [python 3.8](https://www.python.org/)
* [django](https://www.djangoproject.com/)
* [drf](https://www.django-rest-framework.org/)
* [posgresql](https://www.postgresql.org/)
* [docker](https://www.docker.com/)
* [nginx](https://nginx.org/)

## Автор

* **Семенов Денис** - [da-semenov](https://github.com/da-semenov)
* **Сайт:** http://130.193.41.43/api/v1/
