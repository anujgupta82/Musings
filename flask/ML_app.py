#/Users/admin/.virtualenvs/keras_0_3_2

from flask import Flask, jsonify, request, abort 
import pickle
import numpy as np

app = Flask(__name__)

model_file_path = "./../models/final_model.pkl"
model = None


def get_prediction(X): 

	#print X
	#print type(X)
	#print X.shape

	X_i = X.reshape(1, 2)

	print "X_i.shape" 
	print X_i.shape

	#load the model if not already done
	global model
	if model == None:
		model = pickle.load(open(model_file_path, 'rb'))

	#make prediction and return the same
	prediction = model.predict(X_i)[0]

	return prediction


@app.route('/predict', methods=['POST'])
def predict():

	print request.json

	if not request.json or not 'X1' in request.json or not 'X2' in request.json:
		abort(404)

	X1 = request.json['X1']
	X2 = request.json['X2']
	print type(X1), type(X2)

	X1_ = np.float64(X1)
	X2_ = np.float64(X2)

	#print type(X1_), type(X2_)

	X = np.array([X1_, X2_])


	prediction = get_prediction(X)

	return jsonify({'prediction':prediction})


#@app.route('/get_model_params')

#@app.route('/update', methods=['POST'])
if __name__ == '__main__':
	app.run(debug=True)