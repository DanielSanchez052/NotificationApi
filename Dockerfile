FROM python:3.10.8-slim

#set work directory
WORKDIR /code

#set environment variables
ENV PYTHONUNBUFFERED=1
ENV PUTHONDONTWRITEBYTECODE=1

#insall dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy entrypoint.sh
# COPY ./entrypoint.sh .
# RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
# RUN chmod +x /usr/src/app/entrypoint.sh

#copy project
COPY . /code/


# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# # gunicorn
# CMD ["gunicorn", "--config", "gunicorn-cfg.py", "NotificationApi.wsgi"]

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]