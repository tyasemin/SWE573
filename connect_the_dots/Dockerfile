# Dockerfile
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Use netcat-openbsd instead of netcat
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

COPY connect_the_dots/requirements.txt .
RUN pip install --upgrade pip && pip install -r connect_the_dots/requirements.txt

COPY . .

