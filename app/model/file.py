from app.app import app, db
from .base import BaseModel

class FileModel(BaseModel, db.Model):
	"""Model for the file table"""
	__tablename__ = 'file'

	file_uuid = db.Column(db.Text, primary_key=True)
	file_name = db.Column(db.Text)
	file_extension = db.Column(db.Integer)
	date_uploaded = db.Column(db.Text)
	date_modified = db.Column(db.Text)
	file_hash = db.Column(db.Text)
	source_identifier = db.Column(db.Text)
