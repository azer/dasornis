from dasornis.core import HttpHandler
from os.path import dirname
from dasornis.log import logging
from dasornis.template import Template

TEMPLATE = '%s/%s'%(dirname(__file__),'error_template.html')


class ErrorPage(HttpHandler):
  def init(self,*args,**kwargs):
    self.title = 'Unexpected Error'
    self.description = None

  def get(self):
    self.template = Template(self,TEMPLATE,'pythonstring')
    self.template.args.append( ('title',self.title) )
    self.template.args.append( ('description',self.description) )

class HTTPNotFound(ErrorPage):
  def init(self,*args,**kwargs):
    self.title = 'Not Found'
    self.description = 'Could not found given URL.'
    
  def get(self):
    ErrorPage.get(self)
    self.template.args.append( ('excstack','') )

class InternalError(ErrorPage):
  def get(self,excstack):
    ErrorPage.get(self)
    logging.error("INTERNAL ERROR")
    logging.error('  %s'%excstack.type)
    logging.error('  %s'%excstack.value)
    logging.error('  %s'%excstack.format_stack())
    self.template.args.append( ('excstack',excstack) )
    if not self.template.args[3][1]:
      self.template.args[3] = ('description',excstack.value)
