from flask import jsonify
from flask_api import status

def uploadFile():
	return jsonify({}), status.HTTP_200_OK