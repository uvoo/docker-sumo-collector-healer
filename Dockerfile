FROM ubuntu:latest
# FROM python:slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y ansible gettext-base python3 python3-requests

COPY app.py .
COPY main.sh .
COPY rcmd .
COPY vars.yaml.envsubst .

CMD [ "./main.sh" ]
