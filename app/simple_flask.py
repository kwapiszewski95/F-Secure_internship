from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
	if not request.is_json:
		posted_json = request.get_json(force=True)
		return jsonify({"msg": posted_json,"status":"ok"})
	else:
		return jsonify({"status":"error"})


if __name__ == '__main__':
	app.run(debug=True)


