from dasornis.forms.field import Field
from dasornis import exceptions

class Combobox(Field):
  def __init__(self,*args,**kwargs):
    super(Combobox,self).__init__(*args,**kwargs)
    self.type = 'combobox'
    self.is_multiline = False
    self.keys = tuple()
    self._choices = None
    self.choices = kwargs['choices']

  @property
  def choices(self):
    return self._choices

  @choices.setter
  def choices(self,value):
    value_type = type(value[0]) if value and len(value) > 0 else None
    self._choices = value if value_type == tuple or value_type == list else [ (v,v) for v in value ]
    self.keys = [ k for k,v in self._choices ]
    
  def validate(self):
    if not self.value in self.keys:
      raise exceptions.InvalidInput,self
    super(Combobox,self).validate()

