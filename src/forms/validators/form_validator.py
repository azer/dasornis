from dasornis.forms import Validator

class ValidateForm(Validator):
  def __init__(self):
    self.inspectors.append(self.inspect_form)
  
  def inspect_form(self,request_handler,*args,**kwargs):
    for field in request_handler.template.form._fields_:
      if not field.value:
        field.value = request_handler.request.POST.get(field.name)

    for field in request_handler.template.form._fields_:
      field.validate()
