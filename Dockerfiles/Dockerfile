FROM python:3.6-alpine
RUN apk --update add bash nano
RUN apk add postgresql-dev gcc python3-dev musl-dev postgresql libpq postgresql-client build-base linux-headers pcre-dev uwsgi
COPY ./requirements.txt /etc/flask/app/requirements.txt
RUN pip install -r /etc/flask/app/requirements.txt
ARG CONFIG_NAME
COPY ./instance/$CONFIG_NAME /etc/flask/app/$CONFIG_NAME
ENV APP_CONFIG_FILE /etc/flask/app/$CONFIG_NAME
ARG INTERNAL_FILE_STORAGE_PATH
ENV FILE_STORAGE_PATH $INTERNAL_FILE_STORAGE_PATH
COPY ./ /app
CMD ["uwsgi", "--chdir", "/app", "--socket", "0.0.0.0:5000", "--protocol=http", "--module", "main", "--callable", "app", "--enable-threads"]