from flask_restful import Resource
from app.app import api
from typing import List
from app.model import FileModel
from app.app import db

class File():
	def getFiles(self) -> List[FileModel]:
		return []

	def getFile(self, index) -> FileModel:
		return None