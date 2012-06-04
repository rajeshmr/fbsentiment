
from data.model import Status
import data.db as db
from google.appengine.ext import webapp


class Learn(webapp.RequestHandler):
	def post(self):
		status = Status()
		status.message = self.get_message()
		status.sentiment = self.get_sentiment()
		status.pagename = self.get_pagename()
		status.pageid = self.get_pageid()
		db.add_status(status)
		#ret = {'status': 200, 'msg': 'Thanks!'}
	    	#self.spit_json(ret)

	def get_message(self):
		t= self.request.get('message')
		if not t:
		      raise Exception('message is missing')
		return t

	def get_sentiment(self):
		s= self.request.get('sentiment')
		if not s:
		      raise Exception('Sentiment is missing')
		return s
	
	def get_pagename(self):
		p= self.request.get('pagename')
		if not p:
		      raise Exception('Page name is missing')
		return p
	
	def get_pageid(self):
		i= self.request.get('pageid')
		if not i:
		      raise Exception('Page id is missing')
		return i
	
	
