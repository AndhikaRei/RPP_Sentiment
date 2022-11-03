@ECHO OFF
ECHO Setting up virtual environment...
pip install virtualenv
CD ..
python -m venv venv
ECHO Installing requirements...
CALL virt\Scripts\activate
pip install -r requirements.txt
flask db downgrade --directory src/migrations
flask db upgrade --directory src/migrations
flask seed run --root src/seeds
ECHO Setup complete, running app...
CD ./scripts
CALL run
