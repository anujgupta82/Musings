#/Users/admin/.virtualenvs/keras_0_3_2

'''
A simple flask app - This does not implement principles of RESTful

To run this code on terminal :
	Go to Path where this file is saved
	export FLASK_APP=simple_app.py
	flask run
	[If this doesnt work, check flask docs for quickstart]

	You get the path where flask server is running
	Go to browser and type http://127.0.0.1:5000/1 or http://127.0.0.1:5000/2

	This invokes the appropriate function

'''

from flask import Flask

app = Flask(__name__)

@app.route('/1')   # path to resource on server
def index_1():		# action to take
	return "Hello_world 1"

@app.route('/2')
def index_2():
	return "Hello_world 2"

if __name__ == '__main__':
	app.run(debug=True)
