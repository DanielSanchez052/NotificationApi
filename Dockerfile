FROM python:3.10.8-slim

# django-crontab logfile
RUN mkdir /cron
RUN touch /cron/django_cron.log

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONUNBUFFERED=1
ENV PUTHONDONTWRITEBYTECODE=1

# insall dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat cron
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /code/entrypoint.sh
RUN chmod +x  /code/entrypoint.sh

# copy start.sh
COPY ./start.sh .
RUN sed -i 's/\r$//g' /code/start.sh
RUN chmod +x  /code/start.sh

#copy project
COPY . /code/

# # gunicorn
# CMD ["gunicorn", "--config", "gunicorn-cfg.py", "NotificationApi.wsgi"]
RUN service cron start 

ENTRYPOINT ["sh","./entrypoint.sh"]

RUN service cron start

CMD ["sh", "./start.sh"]