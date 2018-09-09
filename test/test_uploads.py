import pytest

from flask import url_for
from flaskext.mysql import MySQL
from flask.wrappers import Request

from libs import uploads

class TestUploads:

	def test_helperfunction(self):
		assert(uploads.helperfunction()==True)