#/Users/admin/.virtualenvs/keras_0_3_2

from flask import Flask, jsonify

app = Flask(__name__)

tasks = [

	{
		'id':1,
		'title':'buy',
		'description':'Buy',
		'done':False	
	},

	{
		'id':2,
		'title':'cook',
		'description':'Cook',
		'done':False
		
	}


]

@app.route('/tasks', methods=['GET'])
def get_tasks():
	return jsonify({'tasks':tasks})


if __name__ == '__main__':
	app.run(debug = True)