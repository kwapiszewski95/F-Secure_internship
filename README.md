<h1>Readme</h1>

To run simple Web Service:
-> app
python simple_flask.py

Example of use:
curl http://127.0.0.1:5000/ -H "Content Type: application/json" -X POST -d '{"myName":"Tomek","type":"This is JSON"}'
