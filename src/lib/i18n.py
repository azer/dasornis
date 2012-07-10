from sys import exc_info
from exception_info import ExceptionInfo
from dasornis import config

class GetText(object):
  def __init__(self,package):
    self.package = package
    self.language = None

  def get_message(self,key):
    result = '#!%s#'%key
    if self.language:
      module = self.package.__dict__[self.language]
      mcontent = module.__dict__
      if mcontent.has_key(key):
        result = mcontent[key]
      else:
        result = '#%s#'%key
    return result 

  def __or__(self,msg_key):
    return self.get_message(msg_key)

get_text = GetText(config.I18N_PACKAGE)
get_text.language = config.DEFAULT_LANG
