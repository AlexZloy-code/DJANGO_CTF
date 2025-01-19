FROM python:3.12.4-slim

RUN apt update
RUN apt install gettext -y

COPY ./requirements /requirements
RUN pip install -r requirements/dev.txt
RUN rm -rf requirements

COPY ./DJANGO_CTF /DJANGO_CTF/
WORKDIR /DJANGO_CTF/

CMD python manage.py makemigrations \
 && python manage.py migrate \
 && python manage.py init_superuser \
 && python manage.py collectstatic --no-input \
 && gunicorn DJANGO_CTF.wsgi:application \
    --timeout 60 \
    --workers 2 \
    --bind 0.0.0.0:8080