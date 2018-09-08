from flask import Flask,request, url_for
from flask import jsonify
from flask import json
from flask_api import status

app = Flask(__name__)

# / routes
@app.route('/', methods=['GET'])
def documentation():
	return jsonify({}), status.HTTP_200_OK

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, use_reloader=False)