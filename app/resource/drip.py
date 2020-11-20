from flask_restx import Resource, Namespace
from flask import send_from_directory
from app.service import Drip as DripService
from app.app import api
from flask_jwt_extended import jwt_required

api = Namespace('drip', description='Drip operations')

@api.route('/<string:file_uuid>')
class Drip(Resource):
	@jwt_required
	def get(self, file_uuid):
		return DripService().getDrip(file_uuid)
