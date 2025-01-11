GNU nano 7.2                                           Dockerfile                                                     FROM python:3.12.4-slim

RUN apt update
RUN apt install gettext -y

COPY ./requirements /requirements
RUN pip install -r requirements/dev.txt
RUN rm -rf requirements

COPY ./Django_CTF /Django_CTF/
WORKDIR /Django_CTF

CMD python manage.py makemigrations \
 && python manage.py migrate \
 && python manage.py init_superuser \
 && python manage.py compilemessages \
 && python manage.py collectstatic --no-input \
 && gunicorn Django_CTF.wsgi:application \
    --workers $(nproc) \
    --bind 0.0.0.0:8000 \