# syntax=docker/dockerfile:1
FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN apk update && apk add postgresql-dev gcc g++ python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt

COPY . /code/

COPY app/docker-entrypoint.sh /docker-entrypoint.sh