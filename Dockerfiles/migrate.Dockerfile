FROM python:3.6-alpine
RUN apk --update add bash nano
RUN apk add postgresql-dev gcc python3-dev musl-dev postgresql libpq postgresql-client build-base linux-headers pcre-dev uwsgi
COPY ./requirements.txt /etc/flask/app/requirements.txt
RUN pip install -r /etc/flask/app/requirements.txt
ARG CONFIG_NAME
COPY ./instance/$CONFIG_NAME /etc/flask/app/$CONFIG_NAME
ENV APP_CONFIG_FILE /etc/flask/app/$CONFIG_NAME
COPY ./ /app
ARG MIGRATION_FOLDER
ENV MIGRATION_FOLDER=$MIGRATION_FOLDER
CMD python3 -B /app/manage.py db migrate --directory=/app/$MIGRATION_FOLDER && python3 -B /app/manage.py db upgrade --directory=/app/$MIGRATION_FOLDER 
