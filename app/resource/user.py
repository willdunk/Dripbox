from flask_restful import Resource
from app.app import api
from flask_restful import Resource, reqparse
from app.model import UserModel, RevokedTokenModel
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
from app.service import User as UserService

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)

@api.resource('/registration')
class UserRegistration(Resource):
	def __init__(self):
		self.service = UserService()

	def post(self):
		return self.service.registerUser(parser.parse_args())

@api.resource('/login')
class UserLogin(Resource):
	def __init__(self):
		self.service = UserService()

	def post(self):
		return self.service.loginUser(parser.parse_args())

@api.resource('/logout/access')
class UserLogoutAccess(Resource):
	def __init__(self):
		self.service = UserService()

	@jwt_required
	def post(self):
		return self.service.logoutUserAccess()

@api.resource('/logout/refresh')
class UserLogoutRefresh(Resource):
	def __init__(self):
		self.service = UserService()

	@jwt_refresh_token_required
	def post(self):
		return self.service.logoutUserRefresh()

@api.resource('/token/refresh')
class TokenRefresh(Resource):
	def __init__(self):
		self.service = UserService()
	
	@jwt_refresh_token_required
	def post(self):
		return self.service.tokenRefresh()

@api.resource('/users')
class AllUsers(Resource):
	def __init__(self):
		self.service = UserService()

	def get(self):
		return self.service.getUsers()

	def delete(self):
		return self.service.deleteUsers()

@api.resource('/secret')
class SecretResource(Resource):
	def __init__(self):
		self.service = UserService()

	@jwt_required
	def get(self):
		return {'answer': 42}
