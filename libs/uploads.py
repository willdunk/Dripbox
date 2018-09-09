from flask import jsonify
from flask_api import status

def uploadFile(_request):
	# Delegator for _request
	return jsonify({}), status.HTTP_200_OK

def helperfunction():
	return True