from flask import Flask, Request, request, url_for
from flask import jsonify
from flask import json
from flask_api import status
from io import BytesIO

from libs import uploads

class MyRequest(Request):
	def _get_file_stream(*args, **kwargs):
		return BytesIO()

def create_app():
	app = Flask(__name__)
	
	app.request_class = MyRequest

	# / routes
	@app.route('/', methods=['GET'])
	def documentation():
		return jsonify({}), status.HTTP_200_OK

	@app.route('/upload', methods=['POST'])
	def upload():
		return uploads.uploadFunction(request)

	return app

if __name__ == "__main__":
	app = create_app()
	app.run(host='0.0.0.0', port=5000, use_reloader=False)