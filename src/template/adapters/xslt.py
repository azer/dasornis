from dasornis.template.adapter import Adapter
from dasornis import exceptions
from re import findall
from os.path import exists as file_exists, isfile,dirname

try:
  import libxml2, libxslt 
except:
  raise exceptions.MissingDependency,'Could not import dependencies (libxml2,libxslt) of XSLT adapter.'

class Adapter(Adapter):
  def __init__(self,*args,**kwargs):
    super(Adapter,self).__init__(*args,**kwargs)

  def load(self):
    self.file = self.lookup()

  def render(self):
    self.load()

    path = dirname(self.file.name)
    xml_doc = libxml2.parseDoc(self.file.read())

    xsl_dec = xml_doc.xpathEval("processing-instruction('xml-stylesheet')") # get xsl decleration firstly
    if not xsl_dec:
      raise exceptions.InvalidXSLDecleration,'Could not found sttylesheet instruction in given xml document'

    xsl_filename = findall('href\=\"([\w\.\/]+)\"',xsl_dec[0].content)
    if not xsl_filename:
      raise exceptions.InvalidXSLDecleration,'Could not found filename of XSL document in href attribute'

    xsl_filename = '%s/%s'%(path,xsl_filename[0])

    if not file_exists(xsl_filename) or not isfile(xsl_filename):
      raise exceptions.InvalidXSLDecleration, 'Could not found XSL file (%s)'%xsl_filename

    xsl_file = libxml2.parseFile(xsl_filename)
    xsl = libxslt.parseStylesheetDoc(xsl_file)

    return xsl.applyStylesheet(xml_doc,{ 'hell':'yeah' })
