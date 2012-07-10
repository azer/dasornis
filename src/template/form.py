import exceptions,patterns
from functools import partial

class FormBase(type):
  def __init__(cls,name,bases,attrs):
    super(FormBase,cls).__init__(name,bases,cls)

  def __call__(cls):
    form = Form.__new__(cls)
    form.__fields__ = []
    for fkey in form.__order__ if hasattr(form,'__order__') else dir(form):
      if not (fkey[0:2]=='__' and fkey[-2:]=='__'):
        field = getattr(form,fkey)()
        setattr(form,fkey,field)
        form.__fields__.append(field)
    return form

class Form(object):
  __metaclass__ = FormBase

