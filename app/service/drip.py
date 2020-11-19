from typing import List
from app.model import FileModel
from app.app import db
import uuid
import datetime
from app.utils import get_digest, get_name, get_extension
import os
from flask import safe_join

class Drip():
	def getDrip(self, file_uuid):
		return FileModel.query.filter_by(file_uuid=file_uuid).first()
