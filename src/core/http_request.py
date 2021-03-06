from cgi import FieldStorage
from dasornis import exceptions

class HttpRequest(object):
  def __init__(self,environ):
    self._get = None
    self._post = None
    self._session = None
    self.META = environ
    self.method = environ.get('REQUEST_METHOD')

  @property
  def GET(self):
    if self._get == None:
      qs = self.META.get('QUERY_STRING','')
      self._get = qs and dict([ (part.count("=") and part or "%s="%part).split("=") for part in qs.split("&") ]) or {}
    return self._get

  @property
  def POST(self):
    if self._post == None:
      fs = FieldStorage(fp=self.META['wsgi.input'],environ=self.META,keep_blank_values=1)
      self._post = dict( [ (key,fs[key].value) for key in fs ] ) or {}

    return self._post
