from dasornis import exceptions

class FieldBase(type):
    def __call__(cls,*args,**kwargs):
      def create_instance(form,attr_name):
        Field._creationCounter_ += 1
        obj = super(Field,cls).__new__(cls,*args,**kwargs)
        obj.__init__(form,Field._creationCounter_,*args,**kwargs)
        setattr(form,attr_name,obj)
        return obj
      return create_instance

class Field(object):
  __metaclass__ = FieldBase
  _creationCounter_ = 0

  def __init__(self,form,index,*args,**kwargs):
    self._form_ = form
    self.index = index
    self.is_required = kwargs['is_required'] if 'is_required' in kwargs else True
    self.is_disabled = kwargs['is_disabled'] if 'is_disabled' in kwargs else False
    self.is_visible = kwargs['is_visible'] if 'is_visible' in kwargs else True
    self.name = kwargs.get('name') or 'formfield%i'%self.index
    self.dom_id = kwargs['dom_id'] if 'dom_id' in kwargs else self.name
    self.label_i18n_key = kwargs['label_i18n_key'] if 'label_i18n_key' in kwargs else self.name
    self.pattern = None
    self.type = None
    self.value = kwargs.get('value')
    self.min_length = kwargs['min_length'] if 'min_length' in kwargs else 0
    self.max_length = kwargs['max_length'] if 'max_length' in kwargs else 0xff
    
  def __cmp__(self,field):
    return cmp(self.index,field.index)

  def __str__(self):
    return '<dasornis.forms.Field name=%s>'%self.name   

  def validate(self):
    if self.is_required and not self.value:
      raise exceptions.MissingInfo,self
    elif self.value and ( not self.min_length<=len(str(self.value))<=self.max_length ):
      raise exceptions.LengthError,self
    elif self.value and self.pattern and not self.pattern.match(str(self.value)):
      raise exceptions.InvalidInput,self
