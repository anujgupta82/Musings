'''
	To run this app, go to the path where this file is there, 
	do - gunicorn <name of the file>
	gunicorn app

	this will get the server up and running - to post a payload, we use poster 'add-on' 
	URL to hit: http://127.0.0.1:8000/hi
'''


import falcon
import functionality

api = application = falcon.API()

hello_world = functionality.hello_world()

api.add_route('/hi', hello_world)