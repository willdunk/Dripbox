from flask_restful import Resource, reqparse
from app.service import File as FileService
from app.app import api
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import helpers

@api.resource('/file', '/file/<string:identifier>')
class File(Resource):
	def __init__(self):
		self.service = FileService()
	
	def get(self, index=None):
		return {"hello": "world"}

	def post(self):
		parse = reqparse.RequestParser()
		parse.add_argument('user_file', type=FileStorage, location='files', action='append')
		parse.add_argument('user_id', type=int, location='args')
		args = parse.parse_args()
		print(args)
		file = args['user_file']
		print(file)
		# if file:
		# 	file.filename = secure_filename(file.filename)
		# 	print(file.filename)
		# 	return {'url': 'hello'}
		return 'Invalid file'
