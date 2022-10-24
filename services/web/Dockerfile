# pull official base image
FROM python:3.9.5-slim-buster

# Docker Work Main 폴더 설정
WORKDIR /usr/src/app

# Python 환경변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip

RUN pip install flask_restx
RUN pip install pandas
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -U flask-paginate
RUN pip install -r requirements.txt
# copy project
COPY . /usr/src/app/

