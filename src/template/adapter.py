"""
Adapter Class for dasornis Framework
"""
from dasornis import exceptions
from os.path import exists as file_exists, isfile

class Adapter(object):
  def __init__(self,template):
    self.template = template
    self.file = None

  def load(self):
    raise exceptions.NotImplemented

  def render(self):
    raise exceptions.NotImplemented

  def lookup(self):
    filename = self.template.filename
    path = '%%s/%s'%filename
    file = None

    if file_exists(filename) and isfile(filename):
      file = open(filename)
    else:
      for dir in self.template.directories:
        if file_exists(path%dir) and isfile(path%dir):
          file = open(path%dir)
          break
    return file
