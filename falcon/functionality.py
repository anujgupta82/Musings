'''

'''

import falcon
import json


class hello_world(object):

	def __init__(self):
		print "init"

	def on_post(self, req, resp):
		print "post: hello_world"
		result = {}
		result['msg'] = "hello world"
		
		resp.status = falcon.HTTP_200
		resp.body = json.dumps(result, encoding='utf-8')


	#def on_get(self, req, resp):


