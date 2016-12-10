#/Users/admin/.virtualenvs/keras_0_3_2

from flask import Flask, jsonify, abort, request

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

# get all tasks 
@app.route('/tasks/', methods=['GET'])
def get_tasks():
	return jsonify({'tasks':tasks})

# get a specific task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_tasks1(task_id):
	task = [task for task in tasks if task['id']==task_id]
	if len(task) == 0:
		abort(404)

	return jsonify({'task':task[0]})  #bcoz task is list

# add a task
@app.route('/tasks/', methods=['POST'])
def create_task():
	#if the incoming request is not a json or doesnt have title, abort

	if not request.json or not 'title' in request.json:
		abort(400)

	print request

	task = {
		'id':tasks[-1]['id']+1,
		#'id':30,
		'title':request.json['title'],
		'description':request.json.get('description',""),
		'done':False
	}

	tasks.append(task)

	return jsonify({'task':task}), 201

# update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
	#find if the given task exists 
	task = [task for task in tasks if task['id'] == task_id]

	if len(task) == 0 or not request.json:
		abort(404)

	task_to_be_updated = task[0]

	#do the update
	task_to_be_updated['title'] = request.json.get('title', task_to_be_updated['title'])
	task_to_be_updated['description'] = request.json.get('description', task_to_be_updated['description'])
	task_to_be_updated['done'] = request.json.get('done', task_to_be_updated['done'])

	return jsonify({'task': task_to_be_updated})



# delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
	#find if the given task exists 
	print request

	task = [task for task in tasks if task['id'] == task_id]

	if len(task) == 0 or not request.json:
		abort(404)

	tasks.remove(task[0])

	return jsonify({'result':True})





if __name__ == '__main__':
	app.run(debug = True)