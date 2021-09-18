FROM python:slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y ansible

COPY app.py .
COPY main.sh .
COPY rcmd .
COPY vars.yaml.envsubst .

CMD [ "./main.sh" ]
