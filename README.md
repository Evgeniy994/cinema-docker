# Django-REST-API-for-cinema-service
Django REST API framework project for cinema service

## Installation

## Please install Python and PostgreSQL beforehand !

```shell
git clone https://github.com/Aleksei-Isaev/Django-REST-API-for-cinema-web-app.git
cd Django-REST-API-for-cinema-web-app
python3 -m venv venv
venv/Scripts/activate (for Windows OC)
pip install -r requirments.txt
set DB_HOST=<your host name>
set DB_NAME=<your db name>
set DB_USER=<your user name>
set DB_PASSWORD=<your db password>
python manage.py migrate
python manage.py runserver
```

## *Debugger:
```shell
export/set DEBUG=True
```

## *Docker:
```shell
docker-compose build
docker-compose up
```

## Features
* Registration by email
* JWT authentication for users (with Throttling)
* Admin panel for managing (genres, actors, movies, halls, cinema-sessions, orders with tickets)
* Swagger documentation for api