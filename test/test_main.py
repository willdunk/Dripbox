import pytest
from flask import url_for

class TestApp:

	def test_(self, client):
		res = client.get(url_for('documentation'))
		assert(res.status_code==200)
		assert(res.json == {})

	def test_upload(self, client):
		res = client.get(url_for('upload'))
		assert(res.status_code==200)
		assert(res.json == {})