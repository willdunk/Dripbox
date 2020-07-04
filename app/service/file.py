from flask_restful import Resource
from app.app import api
from typing import List
from app.model import FileModel
from app.app import db
import uuid
import datetime
from app.utils import get_digest, get_name, get_extension
import os
from flask import safe_join

FILE_STORAGE_PATH = os.getenv('FILE_STORAGE_PATH')

class File():
	def getFiles(self) -> List[FileModel]:
		return FileModel.query.order_by(FileModel.file_name).all()

	def getFile(self, file_uuid) -> FileModel:
		return FileModel.query.filter_by(file_uuid=file_uuid).first()

	def setFile(self, file) -> FileModel:
		digest = get_digest(file)
		f = FileModel(
			file_uuid=str(uuid.uuid4()),
			file_name=str(get_name(file)),
			file_extension=str(get_extension(file)),
			date_uploaded=datetime.datetime.now(),
			date_modified=datetime.datetime.now(),
			file_digest=str(digest),
			source_identifier=str(digest+'.dripbox')
		)
		file.seek(0)
		file_path = os.path.abspath(safe_join(FILE_STORAGE_PATH, digest+'.dripbox'))
		file.save(file_path)
		db.session.add(f)
		db.session.commit()
		return f
