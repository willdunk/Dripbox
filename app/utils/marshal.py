from flask_restx import fields
from app.app import api

file_fields = api.model('File', {
	'file_uuid': fields.String,
	'file_name': fields.String,
	'file_extension': fields.String,
	'date_uploaded': fields.DateTime(dt_format='rfc822'),
	'date_modified': fields.DateTime(dt_format='rfc822'),
})

user_fields = api.model('User', {
	'username': fields.String,
	'files': fields.List(fields.Nested(file_fields))
})
