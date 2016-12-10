#/Users/admin/.virtualenvs/keras_0_3_2

from flask import Flask, jsonify, request, abort 

app = Flask(__name__)

model_file_pth = 
model = None


def get_prediction(X):

	#load the model if not already done
	global model
	if model == None:



	#model is there 

	#do samity check on X

	#make prediction and return the same




@app.route('/predict', methods=['POST'])
def predict():
	if not request.json or not 'X' in request.json:
		abort(404)

	X = request.json['X']
	prediction = get_prediction(X)

	return jsonify({'prediction':prediction})


@app.route('/get_model_params')

@app.route('/update', methods=['POST'])