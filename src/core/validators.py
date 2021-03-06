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

class LoginRequired(Validator):
  def __init__(self): pass

print 'fuck!' 

class FormValidator(Validator):
  def __init__(self,form_class):
    self.form_class = form_class
    self.inspectors.append(self.inspect_form)

    print 'fuck!'
  
  def inspect_form(self,request_handler,*args,**kwargs):
    for field in request_handler.template.form.__fields__:
      if not field.value:
        print field.name,'=======',field.value
        field.value = request_handler.request.POST.get(field.name)
    for field in request_handler.template.form.__fields__:
      field.validate()
