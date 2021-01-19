# Flask, Postgres, Docker app

### Requisitos:
- Se utiliza la imagen base de docker `python:3.9.1-slim-buster`
- En el archivo `docker-compose`, se utiliza la imagen base de docker `postgres:12.4`

### Docker
python manage.py db init
python manage.py db migrate --message 'Initial database migration'
python manage.py db upgrade
python manage.py postal_codes