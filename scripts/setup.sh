#!/bin/bash
pip3 install virtualenv
cd ./../src
virtualenv -p python venv
source venv/bin/activate
pip3 install -r requirements.txt
flask db downgrade
flask db upgrade
flask seed run
cd ./../scripts
./run.sh