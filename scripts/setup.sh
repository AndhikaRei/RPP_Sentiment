#!/bin/bash
pip3 install virtualenv
cd ..
virtualenv -p python venv
source venv/bin/activate
pip3 install -r requirements.txt
flask db downgrade --directory src/migrations
flask db upgrade --directory src/migrations
flask seed run --root src/seeds
cd ./scripts
./run.sh