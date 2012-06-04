from google.appengine.ext.webapp import template
from google.appengine.ext import webapp



class stats(webapp.RequestHanler):
	def get(self):
		self.request.out.write("uc")
