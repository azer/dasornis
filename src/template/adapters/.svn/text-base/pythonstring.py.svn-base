from dasornis.template.adapter import Adapter

class Adapter(Adapter):
  def __init__(self,*args,**kwargs):
    super(Adapter,self).__init__(*args,**kwargs)

  def load(self):
    self.file = self.lookup()

  def render(self):
    self.load()
    return self.file.read()%dict(self.template.args)
