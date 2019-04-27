from flask import Flask, jsonify
from stockstash import app, mongo
 


@app.route("/")
def index():
	return jsonify(message="start test for Ain 1")

# example find_one
@app.route('/read')
def read():
	user = mongo.db.users
	_id = user.find_one({'name' : 'some full name'})
	return 'You found ' + _id['name']

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=True)