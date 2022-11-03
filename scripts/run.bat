@ECHO OFF
CD ..
CALL venv\Scripts\activate
explorer "http://localhost:5000"
flask run
PAUSE