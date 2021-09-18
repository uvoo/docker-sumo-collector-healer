FROM python:slim-buster

WORKDIR /app

# SHELL ["/bin/bash", "-c"]
COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

# COPY . .
COPY rcmd .
COPY app.py .
COPY vars.yaml.envsubst .

CMD [ "main.sh"]
