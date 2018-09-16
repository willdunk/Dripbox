import pytest
import json

from flask import url_for
from flaskext.mysql import MySQL
from flask.wrappers import Request
from io import BytesIO

from libs import uploads

class TestUploads:

	# def test_upload(self, client):
	# 	body = {"filename":"Hellothere.py"}
	# 	mimetype = 'application/json'
	# 	headers = {
	# 		'Content-Type': mimetype,
	# 		'Accept': mimetype
	# 	}
	# 	assert(url_for("upload") == "/upload")
	# 	res = client.post(url_for('upload'), headers=headers, data=json.dumps(body))
	# 	assert(res.content_type == mimetype)
	# 	assert(res.json == body)
	# 	assert(res.status_code==200)

	# def test_helperfunction(self):
	# 	dic = {"filename":"Hellothere.py"}
	# 	assert(uploads.helperfunction(dic)==dic)

	# def test_upload_with_file(self, client):
	# 	assert(url_for("uploadfile") == "/uploadfile")
	# 	res = client.post(url_for('uploadfile'),
	# 		data = {
	# 			'file': (BytesIO(b'my file contents'), 'hello world.txt'),
	# 			'othervalue': "hellothere"
	# 		},
	# 		content_type="multipart/form-data"
	# 	)
	# 	assert({"contents": "my file contents"} == res.json)

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