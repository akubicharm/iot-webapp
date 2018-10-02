FROM python:2.7-jessie

RUN apt-get update

RUN apt-get -y install libboost-all-dev python-dev libboost-python-dev
RUN pip install Flask
RUN pip install azure-iothub-device-client

COPY requirements.txt /

WORKDIR /

RUN pip install -r ./requirements.txt --no-cache-dir

COPY app/ /app/

WORKDIR /app

ENV FLASK_APP=app.py
CMD flask run -h 0.0.0.0 -p 80 
