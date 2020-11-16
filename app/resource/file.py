from flask_restful import Resource, reqparse, marshal_with
from app.service import File as FileService
from app.app import api
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_identity
from app.utils import file_fields

@api.resource('/file')
class NewFile(Resource):
	def __init__(self):
		self.service = FileService()

	@jwt_required
	@marshal_with(file_fields)
	def post(self):
		parse = reqparse.RequestParser()
		parse.add_argument('user_file', type=FileStorage, location='files', action='append')
		parse.add_argument('public')
		username = get_jwt_identity()
		args = parse.parse_args()
		files = args['user_file']
		is_public = bool(args['public'])
		files_processed = []
		for file in files:
			files_processed.append(self.service.setFile(file, username, is_public))
		return files_processed

@api.resource('/file/<string:file_uuid>')
class File(Resource):
	def __init__(self):
		self.service = FileService()

	@jwt_optional
	@marshal_with(file_fields)
	def get(self, file_uuid):
		return self.service.getFile(file_uuid, get_jwt_identity())

	@jwt_required
	@marshal_with(file_fields)
	def post(self, file_uuid):
		parse = reqparse.RequestParser()
		parse.add_argument('user_file', type=FileStorage, location='files', action='append')
		parse.add_argument('public')
		args = parse.parse_args()
		updated_file = args['user_file'][0]
		is_public = bool(args['public'])
		return self.service.updateFile(file_uuid, updated_file, get_jwt_identity(), is_public)
