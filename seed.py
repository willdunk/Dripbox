from flask import Flask,request,redirect, url_for
from flask import jsonify
from flaskext.mysql import MySQL
from datetime import datetime, timedelta

import configparser
import datetime as dt
import time
import uuid
import math
import random

def seed(_preserve):
	configp = configparser.ConfigParser()
	configp.read('dripbox.conf')

	app = Flask(__name__)

	mysql = MySQL()

	DATABASE_NAME = configp.get("Databases", "MysqlDatabase")

	# mySQL initialization
	app.config['MYSQL_DATABASE_USER'] = configp.get("Databases", "MysqlUser")
	app.config['MYSQL_DATABASE_PASSWORD'] = configp.get("Databases", "MysqlPassword")
	# app.config['MYSQL_DATABASE_DB'] = configp.get("Databases", "MysqlDatabase")
	app.config['MYSQL_DATABASE_HOST'] = configp.get("Databases", "MysqlHost")
	app.config['MYSQL_DATABASE_PORT'] = configp.getint("Databases", "MysqlPort")

	# Initialize Connection w/o database
	mysql.init_app(app)
	print("Connected to " + configp.get("Databases", "MysqlHost") + " as " + configp.get("Databases", "MysqlUser"))

	conn = mysql.connect()
	cursor = conn.cursor()

	# Drop database
	temp = ("DROP DATABASE IF EXISTS " + DATABASE_NAME)
	cursor.execute(temp)
	conn.commit()
	print("Dropped old database " + DATABASE_NAME)

	# Create new database
	temp = ("CREATE DATABASE IF NOT EXISTS " + DATABASE_NAME)
	cursor.execute(temp)
	conn.commit()
	print("Created database " + DATABASE_NAME)

	# Add database to config and reinitialize
	app.config['MYSQL_DATABASE_DB'] = DATABASE_NAME
	mysql.init_app(app)
	conn = mysql.connect()
	cursor = conn.cursor()
	print("Connected to " + DATABASE_NAME)

	# candlestick Table
	# Drop old candlestick Table
	temp = ("DROP TABLE IF EXISTS file")
	cursor.execute(temp)
	conn.commit()
	print("Dropped existing candlestick file")
	# Create clients table
	temp = ("CREATE TABLE IF NOT EXISTS file (" + \
		"ufid varchar(50) NOT NULL, " + \
		"PRIMARY KEY (ufid))")
	cursor.execute(temp)
	conn.commit()
	print("Created new file table")

	print("Database config complete")

	# print("Filling in user information")
	# temp = ("INSERT INTO users values (%s, %s, %s, %s, %s, %s, TRUE, %s, %s, NULL)")
	# inputdata = (
	# 	"3534c89a-12d2-11e8-ae1f-c4d987e1e907",
	# 	"username1",
	# 	"John",
	# 	"Smith",
	# 	"jsmith@gmail.com",
	# 	"$2b$12$s5yhFJnsr4s2ZJHwVvZZ2.YsUwJ9TYgwpQgl8x/xwBElRFotVoy9O",
	# 	"2018-03-24 18:46:29",
	# 	"12018675309")
	# cursor.execute(temp, inputdata)
	# conn.commit()
	# print("Filled in users")

seed(False)