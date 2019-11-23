FROM python:3.8.0-alpine3.10

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

CMD flask run --host=0.0.0.0

