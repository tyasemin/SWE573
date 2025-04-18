FROM python:3.8

WORKDIR /code

COPY backend/ /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

