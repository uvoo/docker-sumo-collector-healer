#!/usr/bin/env bash
set -e
echo "Style check."
flake8 app.py

echo "Build and push docker container to Dockerhub."
echo $DOCKERHUB_TOKEN | docker login --username $DOCKERHUB_USERNAME --password-stdin
./buildPush.sh
docker logout
