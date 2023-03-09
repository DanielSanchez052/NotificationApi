FROM python:3.10.8-slim

#copy project
COPY . /code/

#set work directory
WORKDIR /code

#set environment variables
ENV PYTHONUNBUFFERED=1
ENV PUTHONDONTWRITEBYTECODE=1

#insall dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# running migrations
#RUN python manage.py migrate

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "NotificationApi.wsgi"]
