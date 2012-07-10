from functools import partial

class FieldBase(type):
  @staticmethod
  def SetName(cls,index,args,kwargs,name):
    return partial(FieldBase.CreateInstance,cls,name,index,args,kwargs)
  
  @staticmethod
  def CreateInstance(cls,name,index,args,kwargs,entity):
    obj = super(Field,cls).__new__(cls,*args,**kwargs)
    obj.__init__(entity,name,index,*args,**kwargs)
    return obj

  def __call__(cls,*args,**kwargs):
    Field._creationCounter_ += 1
    curried = partial(FieldBase.SetName,cls,Field._creationCounter_,args,kwargs)
    setattr(curried,'DB_FIELD',True)
    return curried

class Field(object):
  __metaclass__ = FieldBase
  _creationCounter_ = 0

  def __init__(self,entity,name,index,*args,**kwargs):
    self.entity = entity
    self.index = index
    self.filters = []
    if kwargs.has_key('filter'):
      self.filters.append(kwargs['filter'])
    self.name = name
    self.type = kwargs.get('type')
    self._value = None

  def __cmp__(self,field):
    return cmp(self.index,field.index)

  def __repr__(self):
    return 'Field[%i,%s]'%(self.index,self.name)

  def filter(self,value):
    for filter in self.filters:
      try:
        value = filter(value)
      except:
        value = filter(**{ 'id':value }) 
    return value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self,value):
    if self.type and not isinstance(value,self.type):
      raise TypeError,'Given value has to be in expected type.'
    self._value = self.filter(value)
