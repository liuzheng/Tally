FROM python:3
COPY ./requirements.txt /tmp/requirements.txt 
RUN pip install -r /tmp/requirements.txt
COPY ./backend/ /opt/app/
WORKDIR /opt/app/
RUN python manage.py collectstatic
ENTRYPOINT /usr/local/bin/uwsgi --ini /opt/app/uwsgi.ini
