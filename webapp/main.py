import webapp2
import os
import jinja2
from google.appengine.ext import ndb


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

class Comments(ndb.Model): #defining comment class to store links of data
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    comment = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class LoginHandler(Handler):
    def get(self):
        self.render("loginpage.html")
        
    
    def post(self):
        login=self.request.get("login")
        password = self.request.get("password")
        
        valid_login={'simi':'austin'}
        if login in valid_login.keys() and valid_login[login]=='austin':
            self.render("default.html")
        else:
            self.render('/loginpage.html',error='Please provide valid username and password')

class MainHandler(Handler):
    def get(self):
        self.render("default.html")
    
class Notes(Handler):
    def get (self):
    	self.render("notes.html")

class Resources(Handler):
	def get (self):
		self.render("resources.html")

class Contact(Handler):
    def get(self):
        self.render("contact_form.html")

class Guestbook(Handler):
    def get(self):
        query = Comments.query().order(Comments.date)
        fetch_five = 5
        comment_list = query.fetch(fetch_five)
        self.render("contact_output.html",comment_list = comment_list)
    def post(self):
        name = self.request.get("name").strip()
        email = self.request.get("email").strip()
        comment = self.request.get("comment").strip()
        error="Please fill out all the above sections!"
        if  name and comment and email:
            guest_book=Comments(name=name,email=email,comment=comment)
            guest_book.put()
            import time
            sleep_sec = 0.1 #assigning variable sleep_sec to 0.1
            time.sleep(sleep_sec)# giving time to datastore to update
            self.redirect('/contact_output')

        else:   
            self.render('contact_form.html',error=error)





app = webapp2.WSGIApplication([
    ('/',LoginHandler),
    ('/default',MainHandler),
    ('/notes',Notes),
	('/resources',Resources),
	('/contact_form',Contact),
    ('/contact_output',Guestbook)
    ], debug=True)
