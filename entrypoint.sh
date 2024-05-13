#!/bin/sh

cd config/
python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn config.wsgi:application --bind 0.0.0.0:8000