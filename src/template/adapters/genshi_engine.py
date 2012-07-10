from os.path import splitext
from dasornis import config, exceptions
from dasornis.template.adapter import Adapter

try:
  from genshi.template import TemplateLoader, NewTextTemplate, MarkupTemplate
  from genshi import Stream
except ImportError:
  raise exceptions.MissingDependency,'Could not import dependencies of Genshi adapter.'

class Adapter(Adapter):
  def __init__(self,*args,**kwargs):
    super(Adapter,self).__init__(*args,**kwargs)
    self.genshi_loader = TemplateLoader(self.template.directories)
    self.file = None
    self.stream = None

  def load(self):
    cls = NewTextTemplate
    name,ext = splitext(self.template.filename)
    if ext=='.html':
      cls = MarkupTemplate
    self.file = self.genshi_loader.load(self.template.filename,cls=cls)

  def render(self):
    self.load()
    self.stream = self.file.generate(**dict(self.template.args))
    name,ext = splitext(self.template.filename)
    if ext=='.html':
      output = self.stream.render('html',doctype='html')
    else:
      output = self.stream.render()
    return output
