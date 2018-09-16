from flask import jsonify, Response
from flask_api import status
from io import BytesIO

# def uploadFunction(_request):
# 	# Delegator for _request
# 	data = _request.get_json()
# 	if (data == None):
# 		return jsonify({'status':'error', 'message':'No body'}), status.HTTP_400_BAD_REQUEST
# 	if ("filename" not in data):
# 		return jsonify({'status':'error', 'message':'Not all required fields present'}), status.HTTP_400_BAD_REQUEST
# 	return jsonify(helperfunction(data)), status.HTTP_200_OK

# def helperfunction(_data):
# 	return {"filename": _data["filename"]};

def uploadFunction(_request):
	# uploaded_files = flask.request.files.getlist("file[]")
	f = _request.files['file']
	assert(type(f.stream) is BytesIO)
	x = f.stream.read()
	return jsonify({}), status.HTTP_200_OK
	# return jsonify({"contents":x.decode("utf-8")}), status.HTTP_200_OK