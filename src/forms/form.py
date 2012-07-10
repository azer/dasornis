from re import match

class FormBase(type):
  def __init__(cls,name,bases,attrs):
    super(FormBase,cls).__init__(name,bases,cls)

  def __call__(cls):
    form = Form.__new__(cls)
    form._fields_ = [ getattr(form,attr_name)(attr_name) for attr_name in dir(form) if not match('_\w+_',attr_name) ]
    form._fields_.sort()
    return form

class Form(object):
  __metaclass__ = FormBase




