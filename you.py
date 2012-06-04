import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp


class You(webapp.RequestHandler):
	def get(self):
		self.redirect("https://apps.facebook.com/fbsentiment/")
