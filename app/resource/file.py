from flask_restx import Resource, reqparse, Namespace
from app.service import File as FileService
from app.app import api
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_identity
from app.utils import file_fields

api = Namespace('file', description='File operations')

parser = reqparse.RequestParser()
parser.add_argument('user_file', type=FileStorage, location='files', action='append')
parser.add_argument('public', type=bool)

@api.route('')
class NewFile(Resource):
	@jwt_required
	@api.expect(parser)
	@api.marshal_with(file_fields)
	def post(self):
		username = get_jwt_identity()
		args = parse.parse_args()
		files_processed = []
		for file in args['user_file']:
			files_processed.append(FileService().setFile(file, username, 'public'))
		return files_processed

@api.route('/<string:file_uuid>')
class File(Resource):
	@jwt_optional
	@api.marshal_with(file_fields)
	def get(self, file_uuid):
		return FileService().getFile(file_uuid, get_jwt_identity())

	@jwt_required
	@api.marshal_with(file_fields)
	def post(self, file_uuid):
		args = parse.parse_args()
		updated_file = args['user_file'][0]
		is_public = bool(args['public'])
		return FileService().updateFile(file_uuid, updated_file, get_jwt_identity(), is_public)
