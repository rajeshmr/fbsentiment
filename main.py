#!/usr/bin/env python

import os
import re

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users

from status_analyzer import StatusAnalyzer
from status_fetcher import StatusFetcher



import data.db as db
import random
import search
import search_results
import analyze
import learn
import you
import about
import admin
import fbapp
import fbtab



class MainHandler(webapp.RequestHandler):
    def get(self):
    	user = users.get_current_user()
	fetcher = StatusFetcher()
	analyzer = StatusAnalyzer()
    	global url,greeting,url_linktext

    	if users.get_current_user():
    		url = users.create_logout_url(self.request.uri)
    		greeting = 'Hi '+user.nickname()
    		url_linktext = 'Logout'
    	else:
    		url = users.create_login_url(self.request.uri)
    		greeting = 'Welcome Guest'
            	url_linktext = 'Login'
        
        trend_col = db.fetch_all_popular()
        id = []
	for x in trend_col:
   		id.append(x.fb_id)
	
        trend_id=random.choice(id)
	trend_wall = fetcher.FetchWall(trend_id)
	cloud = []
	for x in trend_wall.get("data"):
		y = ("%s" % x.get("message")).lower()
		y = re.sub(r'[^A-Za-z]'," ", y)
		cloud.append(y)
	trend_wall_info = fetcher.FetchInfo(trend_id)
	c_trend_wall = analyzer.classify(trend_wall.get("data"))
	stats,agres = analyzer.aggregate(c_trend_wall)
	rusers = analyzer.genRecentUsers(trend_wall.get("data"))
	template_values = {
    		'greeting': greeting,
    		'l_url':url,
    		'url_linktext':url_linktext,
		'pie':stats,
		'trend_img':trend_wall_info.picture,
		'fb_link':trend_wall_info.link,
		'trend_title':trend_wall_info.name,
		'fb_id':trend_wall_info.id,
		'cloud':analyzer.genTags(cloud),
		'tinfo':trend_wall_info,
		'users': rusers,
    	}

	path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
	self.response.out.write(template.render(path,template_values))	

class errors(webapp.RequestHandler):
	def get(self):
		self.response.out.write("Opps, Something went wrong! Please try again later.")
    	
def main():
    application = webapp.WSGIApplication([(r'/', MainHandler),
    					  (r'/search', search.search),
    					  (r'/search-results',search_results.search_results),
    					  (r'/learn',learn.Learn),
    					  (r'/error',errors),
					  (r'/analyze',analyze.analyze),
					  (r'/you',you.You),
					  (r'/about',about.About),
					  (r'/admin',admin.Admin),
					  (r'/fbapp/',fbapp.RecentAnaHandler),
					  (r'/fbapp/user/(.*)', fbapp.UserAnaHandler),
#        				  (r'/fbapp/ana', fbapp.RunHandler),
 #       				  (r'/fbapp/realtime', fbapp.RealtimeHandler),
  #      				  (r'/fbapp/task/refresh-user/(.*)', fbapp.RefreshUserHandler),
					  (r'/fbtab/',fbtab.FBTab)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
