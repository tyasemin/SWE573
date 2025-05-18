# Dockerfile
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Use netcat-openbsd instead of netcat
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

RUN pip install Django>=4.0 psycopg2-binary python-decouple python-dotenv pycountry Pillow

COPY . .

