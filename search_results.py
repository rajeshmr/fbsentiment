
FACEBOOK_APP_ID = "108126969287726"
FACEBOOK_APP_SECRET = "ef11a0a561e77b1c7d1fe2a0025937e8"
import base64
import cgi
import Cookie
import email.utils
import hashlib
import hmac
import logging
import os.path
import time
import urllib
import urlparse
import wsgiref.handlers

import facebook

from google.appengine.ext.webapp import template


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import urlfetch
from django.utils import simplejson as json




class User(db.Model):
    id = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty(required=True)
    profile_url = db.StringProperty(required=True)
    access_token = db.StringProperty(required=True)



class search_results(webapp.RequestHandler):
	access_token ="access_token=108126969287726|H0dVUYy9G3ZPibXTFFOPP7ESUys"
	def get(self):
		#if not users.get_current_user():
		#    	self.redirect('/')
		keyword = self.request.get("keyword")
		if not keyword:
			self.redirect('/')
		keyword.replace(' ','+')
		#args = dict(client_id=FACEBOOK_APP_ID,client_secret=FACEBOOK_APP_SECRET,grant_type='client_credentials')
		# try:
			# response = urlfetch.fetch("https://graph.facebook.com/oauth/access_token?"+urllib.urlencode(args),method=urlfetch.GET,deadline=10)
	        	# access_token = response.content
				
	        # except:
	        	# self.redirect('/error')
		
		results = urlfetch.fetch("https://graph.facebook.com/search?q="+keyword+"&type=page&"+search_results.access_token+"&limit=550",method=urlfetch.GET,deadline=10)
		# obj = json.loads(results.content)
		
		# template_values = {
			# 'results':obj,
    		# }
		
	    	# path = os.path.join(os.path.dirname(__file__), 'templates/search-results.html')
	    	# self.response.out.write(template.render(path,template_values))	
		#self.response.headers.add_header('Set-Cookie','at=%s; expires=Fri, 31-Dec-2020 23:59:59 GMT' % access_token.encode())					
		self.response.out.write(results.content)
