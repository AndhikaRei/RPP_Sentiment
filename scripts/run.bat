@ECHO OFF
CD ./../src
CALL virt\Scripts\activate
explorer "http://localhost:5000"
flask run
PAUSE