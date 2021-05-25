FROM python:3.8.3

RUN mkdir -p /monobank-informer
WORKDIR /monobank-informer

COPY . /monobank-informer

RUN pip install -r requirements.txt
