from flask_restx import Resource, reqparse, marshal_with 
from app.app import api
from app.model import UserModel, RevokedTokenModel
from flask_jwt_extended import jwt_required, jwt_refresh_token_required, get_jwt_identity
from app.service import User as UserService
from app.utils import user_fields

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)

@api.route('/registration')
class UserRegistration(Resource):
	@api.doc(security=None)
	@api.expect(parser)
	def post(self):
		return UserService().registerUser(parser.parse_args())

@api.route('/user')
class User(Resource):
	@jwt_required
	@api.marshal_with(user_fields)
	def get(self):
		return UserService().getUser(get_jwt_identity())

	@api.doc(security=None)
	@api.expect(parser)
	def post(self):
		return UserService().loginUser(parser.parse_args())

@api.route('/logout/access')
class UserLogoutAccess(Resource):
	@jwt_required
	def post(self):
		return UserService().logoutUserAccess()

@api.route('/token/refresh')
class TokenRefresh(Resource):
	@jwt_refresh_token_required
	def post(self):
		return UserService().tokenRefresh()

@api.route('/logout/refresh')
class UserLogoutRefresh(Resource):
	@jwt_refresh_token_required
	def post(self):
		return UserService().logoutUserRefresh()
