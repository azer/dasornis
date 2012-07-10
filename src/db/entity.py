from re import match
from functools import partial
from query import Query
from field import Field

class EntityBase(type):
  def __init__(cls,name,bases,attrs):
    super(EntityBase,cls).__init__(name,bases,cls)
    setattr(cls,'_fields_',[])
    for field_name in attrs:
      if hasattr(attrs[field_name],'DB_FIELD'):
        inst_factory = attrs.get(field_name)(field_name)
        cls._fields_.append(inst_factory)
    
class Entity(object):
  __metaclass__ = EntityBase
  
  def __init__(self):
    self._fields_ = [ field(self) for field in self._fields_ ]
    self._fields_.sort()

  @staticmethod
  def _getAttribute_(cname,obj):
    raw_value = getattr(obj,'_%s'%cname)
    wrapper = obj._wrappers_[cname]
    return wrapper(raw_value)

  def _map_(self,data):
    for i in range(len(data)):
      field = self._fields_[i]
      field.value = data[i]
      setattr(self,field.name,field.value)
