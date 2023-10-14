#!/bin/bash
set -x
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
export DJANGO_SUPERUSER_PASSWORD=adminpassword
python manage.py createsuperuser --noinput --username=admin2 --email=admin2@example.com
unset DJANGO_SUPERUSER_PASSWORD
gunicorn crm.wsgi:application --bind 0.0.0.0:8000
