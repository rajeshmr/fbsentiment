import logging as log
from data.model import Status
from data.model import Popular

def fetch_all_status():
  status = Status.all()
  return status
  
  
def add_status(status):
  stats = fetch_all_status()
  stats.filter('message =', status.message)
  stats.filter('pagename =', status.pagename)
  stats.filter('pageid =', status.pageid)
  for s in stats:
    # There's already a tweet with the same text. just replace it's sentiment
    log.info('Changing existing tweet: %s', status.message)
    s.sentiment = status.sentiment;
    s.put()
    return

  log.info('Adding status: %s' % status.message)
  status.put()	 

def fetch_all_popular():
   popular = Popular.all()
   return popular

def add_popular(fb_id):
   popular = Popular()
   popular.fb_id = fb_id
   popular.put()
