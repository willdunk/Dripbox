import pytest
import json

from flask import url_for
from flaskext.mysql import MySQL
from flask.wrappers import Request
from io import BytesIO

from libs import uploads

class TestUploads:

	def test_upload(self, client):
		data = {
			"filename":"newfile.txt",
			"file": (BytesIO(b'my file contents'), 'hello world.txt'),
		}
		headers = {
			"Content-Type": "multipart/form-data",
			"Accept": "application/json"
		}
		assert(url_for("upload") == "/upload")
		res = client.post(url_for("upload"), headers=headers, data=data)
		assert(res.content_type == "application/json")
		assert(res.status_code == 200)
		assert(res.json == {})