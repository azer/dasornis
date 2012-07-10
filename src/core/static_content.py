from http_handler import HttpHandler
from base_handler import BaseHandler
from dasornis import exceptions

from os import stat as flStat
from os.path import exists,isfile,isdir
from mimetypes import guess_type
from rfc822 import formatdate
from stat import ST_MTIME

class StaticContent(HttpHandler):
  def __new__(cls,path):
    obj = super(BaseHandler,cls).__new__(cls)
    obj.path = path
    return obj

  def get(self,postfix=''):
    path = '%s%s'%(self.path,postfix)
    is_dir,is_file = isdir(path),isfile(path)
    if not ( is_file and exists(path) ):
      raise exceptions.HTTPNotFound, 'Invalid static file: %s'%path

    file = open(path)
    stat = flStat(path)
    content_type = guess_type(path)

    self.response._content = file.readlines()
    self.response.headers['Content-Type'] = content_type and content_type[0] or 'text/plain'
    self.response.headers['Content-Length'] = str(len(self.response.content))
    self.response.headers['Last-Modified'] = formatdate(stat[ST_MTIME])

