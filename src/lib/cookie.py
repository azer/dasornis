from argument_set import ArgumentSet
from re import findall

class CookieHandler(ArgumentSet):
  def __init__(self,http_handler):
    self.http_handler = http_handler
    self.raw_data = http_handler.request.META.get('HTTP_COOKIE') or ''
    self.data = {}
    self.load()

  def load(self):
    for key,value in findall(r'(\w+)\=([^\;]+);?',self.raw_data):
      ArgumentSet.__setitem__(self,key,value)

  def __getitem__(self,key):
    return ArgumentSet.__getitem__(self,key)

  def __setitem__(self,key,value):
    response = self.http_handler.response
    if not response.headers.has_key('Set-Cookie'):
      response.headers['Set-Cookie'] = ''  
    self.http_handler.response.headers['Set-Cookie']+='%s=%s; '%(key,value)
    ArgumentSet.__setitem__(self,key,value)
