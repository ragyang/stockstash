from flask import Flask, jsonify
from stockstash import app
 
@app.route("/")
def index():
	return jsonify(message="start test for Ain 1")
 
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=True)