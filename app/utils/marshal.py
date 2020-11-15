from flask_restful import fields

file_fields = {
	'file_uuid': fields.String,
	'file_name': fields.String,
	'file_extension': fields.String,
	'date_uploaded': fields.DateTime(dt_format='rfc822'),
	'date_modified': fields.DateTime(dt_format='rfc822'),
}

user_fields = {
	'username': fields.String,
	'files': fields.Nested(file_fields)
}
