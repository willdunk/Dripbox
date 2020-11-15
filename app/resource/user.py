from flask_restful import Resource, reqparse, marshal_with 
from app.app import api
from app.model import UserModel, RevokedTokenModel
from flask_jwt_extended import jwt_required, jwt_refresh_token_required, get_jwt_identity
from app.service import User as UserService
from app.utils import user_fields

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

@api.resource('/token/refresh')
class TokenRefresh(Resource):
	def __init__(self):
		self.service = UserService()

	@jwt_refresh_token_required
	def post(self):
		return self.service.tokenRefresh()

@api.resource('/logout/refresh')
class UserLogoutRefresh(Resource):
	def __init__(self):
		self.service = UserService()

	@jwt_refresh_token_required
	def post(self):
		return self.service.logoutUserRefresh()

@api.resource('/user')
class User(Resource):
	def __init__(self):
		self.service = UserService()

	@jwt_required
	@marshal_with(user_fields)
	def get(self, get_jwt_identity):
		return self.service.getUser()
