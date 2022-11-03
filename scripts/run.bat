@ECHO OFF
CD ..
CALL virt\Scripts\activate
explorer "http://localhost:5000"
flask run
PAUSE