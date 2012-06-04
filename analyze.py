import os
import zipimport
import search_results
import types,collections

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from search_results import search_results
from google.appengine.api import urlfetch
from django.utils import simplejson as json

from classifier.bayes import BayesianClassifier
from status_analyzer import StatusAnalyzer
from status_fetcher import StatusFetcher


class analyze(webapp.RequestHandler):
	def get(self):
		id = self.request.get("id")
		c= BayesianClassifier()
		#access_token = self.request.cookies.get('at', '')

		analyzer = StatusAnalyzer()
		fetcher = StatusFetcher()
		info_dict = fetcher.FetchInfo(id)
		data = fetcher.FetchWall(id)
		classified_results = analyzer.classify(data.get("data"))			
			
		template_values = {
			 'id':info_dict.id,
			 'feed':classified_results,
			 'picture':info_dict.picture,
			 'likes':info_dict.likes,
			 'name':info_dict.name,
			 'category':info_dict.category,
    		}
		path = os.path.join(os.path.dirname(__file__), 'templates/analyze.html')
		self.response.out.write(template.render(path,template_values))	
		
				
