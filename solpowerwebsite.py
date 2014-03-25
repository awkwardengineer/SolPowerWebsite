import cgi
import urllib
import webapp2
import jinja2
import os
from google.appengine.api import urlfetch

from google.appengine.ext.webapp import template

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

url = "https://docs.google.com/a/awkwardengineer.com/forms/d/1DtRmiMEiL1DxhO3ikbl4oumNg-D0Nb2APGjC-RT7GOI/formResponse"
    
    
 
class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        
        path= os.path.join(os.path.dirname(__file__), 'index.html')
  
        self.response.out.write(template.render(path,template_values))
        
    def post(self):
        entry729063598 = self.request.get("entry.729063598")
        entry1294472578 = self.request.get("entry.1294472578")
        entry1482860776 = self.request.get("entry.1482860776")
        
        
        form_fields = {
            "entry.729063598": entry729063598,
            "entry.1294472578": entry1294472578,
            "entry.1482860776": entry1482860776
        }
        form_data = urllib.urlencode(form_fields)
        result = urlfetch.fetch(
            url=url,
            payload=form_data,
            method=urlfetch.POST,
            headers={'Content-Type': 'application/x-www-form-urlencoded'})
        
        if result.status_code == 200:
            template_values = {}
        
            path= os.path.join(os.path.dirname(__file__), 'index.html')
  
            self.response.out.write(template.render(path,template_values))
        else:
            self.error(500)



app = webapp2.WSGIApplication([('/',MainPage)])