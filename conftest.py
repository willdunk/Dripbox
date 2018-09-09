import pytest
import requests
import configparser

from flaskext.mysql import MySQL
from main import create_app

import configparser

@pytest.fixture
def app():
	app = create_app()

	configp = configparser.ConfigParser()
	configp.read('dripbox.conf')

	mysql = MySQL()
	app.config['MYSQL_DATABASE_USER'] = configp.get("Databases", "MysqlUser")
	app.config['MYSQL_DATABASE_PASSWORD'] = configp.get("Databases", "MysqlPassword")
	app.config['MYSQL_DATABASE_DB'] = configp.get("Databases", "MysqlDatabase")
	app.config['MYSQL_DATABASE_HOST'] = configp.get("Databases", "MysqlHost")
	app.config['MYSQL_DATABASE_PORT'] = configp.getint("Databases", "MysqlPort")

	app.debug = True
	return app