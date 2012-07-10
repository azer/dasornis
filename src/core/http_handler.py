from base_handler import BaseHandler
from http_response import HttpResponse
from report import Report
from dasornis.lib.cookie import CookieHandler
from dasornis.template import Template
from dasornis import config

class HttpHandler(BaseHandler):
  '''
  Main Http Handler Class which will be extended by request handlers.
  '''
  def __call__(self,request,*args,**kwargs):
    """
    Works when controller executes mapped subclass
    """
    #super(BaseHandler,self).__call__(request)
    self._template = None
    self.response = HttpResponse()
    self.request = request
    self.report = Report()
    self.cookies = CookieHandler(self)
    self.init(*args,**kwargs)
    """
    Subclasses will have get and post methods to handle requests.
    This method executes these methods by "method" attribute of request object.
    """
    getattr(self,'post' if self.request.method=='POST' else 'get')(*args,**kwargs)
    if self.template:
      self.response.write(self.template.render())
    return self.response

  def init(self,*args): pass
  def get(self,*args,**kwargs): pass
  def post(self,*args,**kwargs): 
    self.get(*args,**kwargs)

  def redirect(self,url):
    self.response.status = '307 Temporary Redirect'
    self.response.headers['Location'] = url

  @property
  def template(self):
    return self._template
    
  @template.setter
  def template(self,template):
    self._template = template
