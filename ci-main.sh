#!/usr/bin/env bash
set -e

echo "Style check."
pip install flake8 && flake8 app.py

echo "Build and push docker container to Dockerhub."
release=latest
repo=uvoo/sumo-collector-healer
tag=$repo:${release}
echo $DOCKERHUB_TOKEN | docker login --username $DOCKERHUB_USERNAME --password-stdin
docker build --tag ${tag} .
docker push ${tag}
docker logout
