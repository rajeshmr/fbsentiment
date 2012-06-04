from google.appengine.ext import db

class Status(db.Model):
  message = db.StringProperty(multiline=True)
  sentiment = db.StringProperty() # one of pos/neg/neu
  pagename = db.StringProperty() # The query in context when storing this tweet
  pageid = db.StringProperty()

class Popular(db.Model):
  fb_id= db.StringProperty()
