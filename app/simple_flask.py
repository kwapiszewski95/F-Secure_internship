from flask import Flask, jsonify, request
from random import randint

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
	if request.is_json:
		posted_json = request.get_json(force=True)
		return jsonify({"msg": posted_json,"status":"ok"})
	else:
		return jsonify({"status":"error"})

@app.route('/random', methods=['GET'])
def getRandom():
	return jsonify({"status":"ok","number":randint(0,100)})


if __name__ == '__main__':
	app.run(debug=True)


