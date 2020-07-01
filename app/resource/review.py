from flask_restful import Resource, fields, marshal_with
import feedparser
from app.service import Review as ReviewService
from app.app import api

review_fields = {
	'review_id': fields.String,
	'title': fields.String,
	'rating': fields.Integer,
	'review_link': fields.String,
	'movie_link': fields.String,
	'banner_image_link': fields.String,
	'content': fields.String,
	'published_date': fields.DateTime(dt_format='rfc822'),
	'watched_date': fields.DateTime(dt_format='rfc822'),
}

@api.resource('/review', '/review/<string:index>')
class Review(Resource):
	def __init__(self):
		self.service = ReviewService()
	
	@marshal_with(review_fields)
	def get(self, index=None):
		if index is None:
			return self.service.getReviews()
		else:
			return self.service.getReview(index)
