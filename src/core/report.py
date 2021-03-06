from dasornis.log import logging
from dasornis.lib.exception_info import ExceptionInfo
from dasornis.lib.argument_set import ArgumentSet
import sys 

class Report(object):
  def __init__(self,**kwargs):
    self._report_type = kwargs.get('report_type')
    self.args = ArgumentSet()
    self.message = None
    self.message_key = None
    self.exception = None
    self.log = False

  @property
  def report_type(self):
    return self._report_type

  @report_type.setter
  def report_type(self,value):
    self._report_type = value

    if self.report_type == Report.ERROR:
      self.exception = ExceptionInfo(sys.exc_info())

      if not self.message_key:
        self.message_key = 'error_unexpected'

      if self.log == True:
        self.exception.log()

    elif self.log:
      logging.info(self.message or self.message_key)

  SUCCESS,WARNING,ERROR = range(101,104)

  class SUCCESS: pass
  class WARNING: pass
  class ERROR: pass
