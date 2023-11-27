FROM python:3.8

RUN echo "Django Course deploy 2023.11.21 21:00"

WORKDIR /home/

RUN git clone https://github.com/updaun/django_course.git -b kmgyu

WORKDIR /home/django_course/

RUN pip install -r requirements.txt

RUN apt update

EXPOSE 8000

CMD ["bash", "-c", "git pull && python manage.py collectstatic --noinput --settings=config.settings.deploy && python manage.py migrate --settings=config.settings.deploy && gunicorn config.wsgi --env DJANGO_SETTINGS_MODULE=config.settings.deploy --bind 0.0.0.0:8000 --timeout 60"]