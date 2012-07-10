class BaseHandler(object):
  def __init__(self,*args):
    pass
  def __new__(cls,*args):
    obj = super(BaseHandler,cls).__new__(cls)
    return obj(*args)
