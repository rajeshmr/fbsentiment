import os

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users



class search(webapp.RequestHandler):
	def get(self):
#		if not users.get_current_user():
#		    	self.redirect('/')

		template_values = {
    		}
				
	    	path = os.path.join(os.path.dirname(__file__), 'templates/search.html')
	    	self.response.out.write(template.render(path,template_values))	
