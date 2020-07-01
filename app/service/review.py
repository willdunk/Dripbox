from flask_restful import Resource
from app.app import api
from typing import List
from app.model import ReviewModel
from app.app import db

class Review():
	def getReviews(self) -> List[ReviewModel]:
		return ReviewModel.query.order_by(ReviewModel.title).all()

	def getReview(self, index) -> ReviewModel:
		return ReviewModel.query.filter_by(review_id=index).first()