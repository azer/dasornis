import traceback
from dasornis.log import logging

class ExceptionInfo(object):
  def __init__(self,exc=None):
    if exc==None:
      if not globals().has_key('sys'):
        import sys
      exc = sys.exc_info()
      
    self.type = exc[0]
    self.value = exc[1]
    self.tb = exc[2]
    self.stack = traceback.extract_tb(self.tb)
    
  def __str__(self):
    return self.format_stack()

  def format_stack(self,ch='\n'):
    return ch.join(traceback.format_exception(self.type,self.value,self.tb))

  def log(self):
    logging.error('EXCEPTION INFO: type: %s, file:%s, function:%s, line: %i, message: %s'%(
      str(self.type),self.stack[-1][0],self.stack[-1][2],self.stack[-1][1],self.value.message
      )
    )
