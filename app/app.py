from flask import Blueprint, url_for
from flask_jwt_extended import JWTManager
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

authorizations = {
	'jwt': {
		'type': 'apiKey',
		'in': 'header',
		'name': 'Authorization',
		'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
	}
}


class PatchedApi(Api):
	@property
	def specs_url(self):
		return url_for(self.endpoint('specs'))

app = Flask(__name__, instance_relative_config=True)
CORS(app)
# app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = PatchedApi(blueprint, doc='/doc/', title="Dripbox", authorizations=authorizations, security='jwt')

app.register_blueprint(blueprint)

app.config.from_object('config')
app.config.from_envvar('APP_CONFIG_FILE')
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['RESTX_MASK_SWAGGER'] = False

jwt = JWTManager(app)
db = SQLAlchemy(app)

from app.resource.user import api as user_ns
from app.resource.file import api as file_ns
from app.resource.drip import api as drip_ns
api.add_namespace(user_ns)
api.add_namespace(file_ns)
api.add_namespace(drip_ns)
