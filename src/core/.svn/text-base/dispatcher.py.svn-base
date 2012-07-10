from http_request import HttpRequest
from dasornis import exceptions
from dasornis.lib.exception_info import ExceptionInfo

class Dispatcher(object):
  
  def __init__(self,map):
    self.url_map = map
   
  def __call__(self,environ,start_response):
    req = HttpRequest( environ )
    try:
      url = environ.get('PATH_INFO')
      handler,args = self.url_map.match(url)
      args = list(args)
      args.insert(0,req)
      response = handler(*args)
    except exceptions.HTTPNotFound:
      from dasornis.extras import pages
      response = pages.HTTPNotFound(req)
    except:
      from dasornis.extras import pages
      response = pages.InternalError(req,ExceptionInfo())

    start_response(response.status,response.headers.items())
    return response
