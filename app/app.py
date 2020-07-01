from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

app = Flask(__name__, instance_relative_config=True)
CORS(app)
api = Api(app)
app.config.from_object('config')
app.config.from_envvar('APP_CONFIG_FILE')

db = SQLAlchemy(app)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

from app.resource import Review as ReviewResource
