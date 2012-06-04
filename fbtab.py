from google.appengine.ext import webapp


class FBTab(webapp.RequestHandler):
	def post(self):
		self.response.out.write("Under construction")
