from dasornis.forms.field import Field

class Passwordbox(Field):
  def __init__(self,*args,**kwargs):
    super(Passwordbox,self).__init__(*args,**kwargs)
    self.type = 'password'
    self.is_multiline = False
