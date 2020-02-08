<h1>Readme</h1>

Note from author: I was not able to continue with Docker-related tasks, due to some problems with virtual machine I'm using. Also time for solving those exercises wasn't best for me because of exam session on University (my last two exams are on Monday). 
Despite that I hope you will give me a chance and invite me for interview - you won't be disappointed :)

<h2>Simple app</h2>

To use simple application go to /app and run python code:
python simple_flask.py

Usage /random endpoint (get random value):
	
	curl http://127.0.0.1:5000/random

Usage /echo endpoint (send and reveive JSON):

	
	curl -X POST -H "Content-Type: application/json" -d '{"username":"abc","password":"abc"}' http://127.0.0.1:5000

OR use Postman (chrome add-on)
