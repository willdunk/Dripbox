from flask_restful import Resource
from app.app import api

@api.resource('/version')
class Version(Resource):
	def get(self):
		return {"version": "1.0"} 