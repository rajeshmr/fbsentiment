from google.appengine.ext import webapp
from google.appengine.api import users
import os
from google.appengine.ext.webapp import template
import data.db as db


class Admin(webapp.RequestHandler):
	def get(self):
	    	user = users.get_current_user()
	    	if not users.get_current_user():
	    		self.redirect(users.create_login_url(self.request.uri))
	    	else:
		    	if user.nickname() == "rraj19":
				template_values = {}
				path = os.path.join(os.path.dirname(__file__), 'templates/admin.html')
			    	self.response.out.write(template.render(path,template_values))	
			else:
				self.response.out.write("You are not authorized!")		
	def post(self):
		user = users.get_current_user()
		if user.nickname() == "rraj19":
			db.add_popular(self.request.get("popular"))
			self.response.out.write("Added to DS")
		else:
			return False	
