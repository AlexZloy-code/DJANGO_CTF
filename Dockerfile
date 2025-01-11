FROM python:3.12.4-slim

RUN apt update
RUN apt install gettext -y

COPY ./requirements /requirements
RUN pip install -r requirements/dev.txt
RUN rm -rf requirements

COPY ./DJANGO_CTF /DJANGO_CTF/
WORKDIR /DJANGO_CTF

CMD python manage.py makemigrations \
 && python manage.py migrate \
 && python manage.py init_superuser \
 && python manage.py compilemessages \
 && python manage.py collectstatic --no-input \
 && gunicorn DJANGO_CTF.wsgi:application \
    --workers $(nproc) \
    --bind 0.0.0.0:8000 \