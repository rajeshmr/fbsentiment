

from google.appengine.ext import webapp
import logging as log
from django.utils import simplejson as json
from google.appengine.api import urlfetch
import types,collections




class AttrDict(dict):

	def __init__(self, *argz, **kwz):
		if len(argz) == 1 and not kwz and isinstance(argz[0], types.StringTypes):
			super(AttrDict, self).__init__(open(argz[0]))
		else:
			super(AttrDict, self).__init__(*argz, **kwz)
			for k,v in self.iteritems(): setattr(self, k, v) # re-construct all values via factory

	def __val_factory(self, val):
		return AttrDict(val) if isinstance(val, dict) else val
	def __getattr__(self, k):
		return super(AttrDict, self).__getitem__(k)
		__getitem__ = __getattr__

	def __setattr__(self, k, v):
		return super(AttrDict, self).__setitem__(k, self.__val_factory(v))
		__setitem__ = __setattr__




class StatusFetcher:
	access_token ="access_token=108126969287726|H0dVUYy9G3ZPibXTFFOPP7ESUys"
	def FetchInfo(self, id):
		try:
			info = urlfetch.fetch("https://graph.facebook.com/"+id+"?"+StatusFetcher.access_token+"&limit=550",method=urlfetch.GET,deadline=10)
			if info.status_code == 200:
				info_dict = AttrDict(json.loads(info.content))
				return info_dict
			else:		
				log.error("Fetch error - info")	
		except urlfetch.Error, e:
			log.error("Exception when contacting twitter %s", e)
		return None
		
		
		
		
	def FetchWall(self,id):
		try:
			results = urlfetch.fetch("https://graph.facebook.com/"+id+"/feed?"+StatusFetcher.access_token+"&limit=550",method=urlfetch.GET,deadline=10)
			data = AttrDict(json.loads(results.content))
			return data

		except:
			log.error("Fetch Error - wall")
		return None
	
