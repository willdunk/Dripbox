from app.app import db
from app.model import ReviewModel
import feedparser
import uuid
from bs4 import BeautifulSoup
import requests
from dateutil.parser import parse

def delta_rss():
	print("Retrieving RSS")
	feed = feedparser.parse('https://letterboxd.com/hahaveryfun/rss/')
	entries = list(filter(lambda entry: 'letterboxd-review' in entry.id, feed.entries))
	for entry in entries:
		review = ReviewModel.query.filter_by(title=entry.letterboxd_filmtitle).first()
		if review is None:
			r = ReviewModel(
				review_id=str(uuid.uuid4()),
				title=str(entry.letterboxd_filmtitle),
				rating=int(float(entry.letterboxd_memberrating)*2),
				review_link=str(entry.link),
				movie_link=str(entry.link),
				banner_image_link=str(parseLetterboxdPage(entry.link)),
				content=str(entry.description),
				published_date=parse(entry.published),
				watched_date=parse(entry.letterboxd_watcheddate),
			)
			db.session.add(r)
		db.session.commit()

def parseLetterboxdPage(review_link):
	text = requests.get(review_link.replace("/hahaveryfun", "")).text
	soup = BeautifulSoup(text, 'html.parser')
	return soup.body.div.div['data-backdrop2x']
