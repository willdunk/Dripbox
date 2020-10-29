from flask_restful import Resource, reqparse, fields, marshal_with
from app.service import File as FileService
from app.app import api
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import helpers

file_fields = {
	'file_uuid': fields.String,
	'file_name': fields.String,
	'file_extension': fields.String,
	'date_uploaded': fields.DateTime(dt_format='rfc822'),
	'date_modified': fields.DateTime(dt_format='rfc822'),
}

@api.resource('/file', '/file/<string:file_uuid>')
class File(Resource):
	def __init__(self):
		self.service = FileService()
	
	@marshal_with(file_fields)
	def get(self, file_uuid=None):
		if (file_uuid is None):
			return self.service.getFiles()
		return self.service.getFile(file_uuid)

	@marshal_with(file_fields)
	def post(self):
		parse = reqparse.RequestParser()
		parse.add_argument('user_file', type=FileStorage, location='files', action='append')
		parse.add_argument('secret')
		args = parse.parse_args()
		files = args['user_file']
		secret = args['secret']
		files_processed = [];
		for file in files:
			files_processed.append(self.service.setFile(file, secret))
		return files_processed
