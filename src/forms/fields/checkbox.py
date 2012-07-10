from dasornis.forms.field import Field

class Checkbox(Field):
  def __init__(self,*args,**kwargs):
    super(Checkbox,self).__init__(*args,**kwargs)
    self.type = 'checkbox'
