from dasornis.forms.field import Field

class Textbox(Field):
  def __init__(self,*args,**kwargs):
    super(Textbox,self).__init__(*args,**kwargs)
    self.type = 'text'
    self.is_multiline = kwargs['is_multiline'] if kwargs.has_key('is_multiline') else False

