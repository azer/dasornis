class QueryResult(tuple):
    def __init__(self,*args,**kwargs):
      tuple.__init__(*args,**kwargs)
      self.query = None

    def __getitem__(self,index):
      value = tuple.__getitem__(self,index)
      if self.query and self.query.entity:
        value = self.query.entity()
        value._map_(tuple.__getitem__(self,index))
      return value

    def __iter__(self):
      for i in range(len(self)):
        yield self.__getitem__(i)
