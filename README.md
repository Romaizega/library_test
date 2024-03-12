# WEB-приложение "Library"
### для создания мероприятий


## Стек технологий
 [![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=e8b600&color=065535)](https://docs.python.org/release/3.9.10)

 [![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=065535 )](https://www.djangoproject.com/)

 [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=3d85c6)](https://www.postgresql.org/)


### Рекомендации по развертыванию проекта локально

Клонируем проект:

```bash
git clone https://github.com/Romaizega/library_test.git
```

Переходим в папку с проектом:

```bash
cd library_test
```

Установить виртуальное окружение:

linux
```bash
python3 -m venv env
```
windows
```bash
python -m venv venv
```
Активировать виртуальное окружение:

linux
```bash
source venv/bin/activate
```
windows
```bash
source venv/Script/activate
```
Установить зависимости:

linux
```bash
python3 -m pip install --upgrade pip
```
windows
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

+ Установить локально [Docker compose](https://www.docker.com/)
+ Создать файлы .env в папках library и infra 
```
POSTGRES_USER=library_user
POSTGRES_DB=django
POSTGRES_PASSWORD=library_password
DB_HOST=db
SECRET_KEY=(SECRET_KEY)
ALLOWED_HOSTS=(ALLOWED_HOSTS)
DEBUG=False
```
+ Запустить проект через `docker compose up`:
```shell script
cd foodgram-project-react/infta
```

```shell script
docker compose  up --build
```


+ Запустить backend сервер:
```shell script
cd backend/
```
```shell script
python manage.py migrate
```
```shell script
python manage.py runserver
```
```shell script
python manage.py createsuperuser