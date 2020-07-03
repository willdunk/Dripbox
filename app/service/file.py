from flask_restful import Resource
from app.app import api
from typing import List
from app.model import FileModel
from app.app import db
import uuid
import datetime
import hashlib

class File():
	def getFiles(self) -> List[FileModel]:
		return FileModel.query.order_by(FileModel.file_name).all()

	def getFile(self, file_uuid) -> FileModel:
		return FileModel.query.filter_by(file_uuid=file_uuid).first()

	def setFile(self, file) -> FileModel:
		BLOCK_SIZE = 65536  # The size of each read from the file

		# Create the hash object, can use something other than `.sha256()` if you wish
		file_hash = hashlib.sha256()
		fb = file.read(BLOCK_SIZE)
		while len(fb) > 0:  # While there is still data being read from the file
			file_hash.update(fb)  # Update the hash
			fb = file.read(BLOCK_SIZE)  # Read the next block from the file
		
		print(file_hash.hexdigest())  # Get the hexadecimal digest of the hash
		
		f = FileModel(
			file_uuid=str(uuid.uuid4()),
			file_name=str(file.filename),
			file_extension=str("py"),
			date_uploaded=datetime.datetime.now(),
			date_modified=datetime.datetime.now(),
			file_hash=str(uuid.uuid4()),
			source_identifier=str(uuid.uuid4())
		)
		db.session.add(f)
		db.session.commit()
		return f
