import unittest
import sys,os.path
sys.path.append(os.path.dirname(__file__)+'../')
from dasornis.template import Template

class TestHelloWorld(unittest.TestCase):
    def testPythonString(self):
        doc = Template('hello_world.ps','pythonstring')
        doc.args.append( ('msg','Hello World!') )
        self.assertEqual(doc.render(),'<h1>Hello World!</h1>\n')

    def testXSLT(self):
      doc = Template('xml/catalog.xml','xslt')

if __name__ == '__main__':
    unittest.main()