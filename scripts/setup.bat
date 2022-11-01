@ECHO OFF
ECHO Setting up virtual environment...
pip install virtualenv
CD ./../src
python -m venv virt
ECHO Installing requirements...
CALL virt\Scripts\activate
pip install -r requirements.txt
flask db downgrade
flask db upgrade
flask seed run
ECHO Setup complete, running app...
CD ./../scripts
CALL run
