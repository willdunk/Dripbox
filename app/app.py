from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
CORS(app)
api = Api(app)
app.config.from_object('config')
app.config.from_envvar('APP_CONFIG_FILE')

db = SQLAlchemy(app)

from app.resource import Drip as DripResource
from app.resource import File as FileResource
