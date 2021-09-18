#!/usr/bin/env bash
set -e
envsubst < vars.yaml.envsubst > vars.yaml
python3 app.py
