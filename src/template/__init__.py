from dasornis.lib.argument_set import ArgumentSet
from dasornis.lib.exception_info import ExceptionInfo
from dasornis.lib.i18n import get_text
from dasornis.lib import get_date
from dasornis.log import logging
from dasornis import config,exceptions
from imp import load_module

class Template(object):
  def __init__(self,request_handler,filename=None,engine=config.TEMPLATE_ENGINE):
    self.form = None
    self.filename = filename
    self.engine_name = engine
    self.request_handler = request_handler
    self.args = [
      ('config',config),
      ('cookies',self.request_handler.cookies),
      ('i18n',get_text),
      ('report',self.request_handler.report),
      ('request',self.request_handler.request),
      ('template',self),
    ]
    self.directories = config.TEMPLATE_DIRS
    
    try:
      engine_path = '%s/template/adapters/%s.py'%(config.DASORNIS_WORKING_DIR,self.engine_name)
      self.adapter_module = load_module(self.engine_name,open(engine_path),engine_path,( '.py', 'U', 1 ))
    except ImportError,IOError:
      raise exceptions.TemplateAdapterDoesntExist,'Unsupported template engine "%s"'%self.engine_name
    
    self.adapter = self.adapter_module.Adapter(self)

  @property
  def filename(self):
    return self._filename

  @filename.setter 
  def filename(self,filename):
    self._filename = filename

  def render(self):
    return self.adapter.render()

