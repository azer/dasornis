class Validator(object):
  def __new__(cls,*args,**kwargs):
    obj = super(Validator,cls).__new__(cls)
    setattr(obj,'inspectors',[])
    return obj

  def __call__(self,rq_method):
    def wrapper(request_handler,*args,**kwargs):
      for inspector in self.inspectors:
        inspector(request_handler,*args,**kwargs)
      return rq_method(request_handler,*args,**kwargs)
    return wrapper
