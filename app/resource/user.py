from flask_restx import Resource, reqparse, marshal_with, Namespace
from app.model import UserModel, RevokedTokenModel
from flask_jwt_extended import jwt_required, jwt_refresh_token_required, get_jwt_identity
from app.service import User as UserService
from app.utils import user_fields

api = Namespace('user', description='User operations')

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)

@api.route('/register')
class Register(Resource):
	@api.doc(security=None)
	@api.expect(parser)
	def post(self):
		return UserService().register(parser.parse_args())

@api.route('/login')
class Login(Resource):
	@api.doc(security=None)
	@api.expect(parser)
	def post(self):
		return UserService().login(parser.parse_args())

@api.route('/info')
class Info(Resource):
	@jwt_required
	@api.marshal_with(user_fields)
	def get(self):
		return UserService().get(get_jwt_identity())

@api.route('/logout/access')
class LogoutAccess(Resource):
	@jwt_required
	def post(self):
		return UserService().logoutAccess()

@api.route('/token/refresh')
class TokenRefresh(Resource):
	@jwt_refresh_token_required
	def post(self):
		return UserService().tokenRefresh()

@api.route('/logout/refresh')
class LogoutRefresh(Resource):
	@jwt_refresh_token_required
	def post(self):
		return UserService().logoutRefresh()
