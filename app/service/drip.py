from app.model import FileModel
from flask_restx import abort
from app.utils.constants import FILE_STORAGE_PATH
from flask import send_from_directory

class Drip():
	def getDrip(self, file_uuid):
		file = FileModel.query.filter_by(file_uuid=file_uuid).first()
		if file:
			return send_from_directory(
				FILE_STORAGE_PATH,
				file.source_identifier,
				as_attachment=True,
				attachment_filename=".".join([file.file_name, file.file_extension]))
		abort(404, message="Not Found")
