from flask_restful import Resource, reqparse, fields, marshal_with
from app.service import File as FileService
from app.app import api
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import helpers

review_fields = {
	'review_id': fields.String,
	'title': fields.String,
	'rating': fields.Integer,
	'review_link': fields.String,
	'movie_link': fields.String,
	'banner_image_link': fields.String,
	'content': fields.String,
	'published_date': fields.DateTime(dt_format='rfc822'),
	'watched_date': fields.DateTime(dt_format='rfc822'),
}

@api.resource('/file', '/file/<string:file_uuid>')
class File(Resource):
	def __init__(self):
		self.service = FileService()
	
	@marshal_with(review_fields)
	def get(self, file_uuid=None):
		if (file_uuid is None):
			return self.service.getFiles()
		return self.service.getFile(file_uuid)

	def post(self):
		parse = reqparse.RequestParser()
		parse.add_argument('user_file', type=FileStorage, location='files', action='append')
		parse.add_argument('user_id', type=int, location='args')
		args = parse.parse_args()
		files = args['user_file']
		for file in files:
			self.service.setFile(file)
		return 'Invalid file'
