class ArgumentSet(dict):
  def set(self,key,value):
    return self.__setitem__(key,value)
