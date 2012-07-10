from re import match
from dasornis import exceptions

class URLMap(list):
  def __init__(self,*urls):
    super(list,self).__init__()
    for url in urls:
      if not isinstance(url,URL) and isinstance(url,tuple):
        url = URL(pattern=url[0],value=url[1])
      self.append(url)

  def match(self,text):
    handler = None
    args = None

    for url in self:
      res = match(url.pattern,text)
      if res:
        handler = url.value
        args = res.groups()

        if isinstance(handler,URLMap):
          end = res.end()
          handler,sub_args = handler.match(text[end:])
          args += sub_args

        return handler,args

    raise exceptions.HTTPNotFound

  def __repr__(self):
    urls = ','.join([ url.__repr__() for url in self ])
    return '<URLMAP file=%s />'%urls

class URL(object):
  def __init__(self,**kwargs):
    self.pattern = kwargs.get('pattern')
    self.value = kwargs.get('value')

  def __repr__(self):
    return '<URL pattern=%s>'%(self.pattern)