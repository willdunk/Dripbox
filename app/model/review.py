from app.app import app, db
from .base import BaseModel

class ReviewModel(BaseModel, db.Model):
	"""Model for the review table"""
	__tablename__ = 'review'

	review_id = db.Column(db.Text, primary_key=True)
	title = db.Column(db.Text)
	rating = db.Column(db.Integer)
	review_link = db.Column(db.Text)
	movie_link = db.Column(db.Text)
	banner_image_link = db.Column(db.Text)
	content = db.Column(db.Text)
	published_date = db.Column(db.DateTime)
	watched_date = db.Column(db.DateTime)
