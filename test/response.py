from cgi import parse_qs, escape
import sys,os.path
sys.path.append(os.path.dirname(__file__)+'../')
from dasornis.core.http_response import HttpResponse

def hello_world(environ,start_response):
  start_response('200 OK', [('Location', 'http://google.com')])
  return HttpResponse('SPAM')

if __name__=='__main__':
  from wsgiref.simple_server import make_server
  srv = make_server('localhost', 8080, hello_world)
  srv.serve_forever()
