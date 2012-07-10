import unittest,sys,os.path
sys.path.append(os.path.dirname(__file__)+'../')
from dasornis.core.urlmap import URLMap
import unittest
from pdb import set_trace

reqhandler1,reqhandler2,reqhandler3,reqhandler4,reqhandler5 = lambda *args: args, lambda *args: args, lambda *args: args, lambda *args: args, lambda *args: args
print('=====')
print('HANDLER ID\'S >> 1:',reqhandler1,id(reqhandler1),' 2:',reqhandler2,id(reqhandler2),' 3:',reqhandler3,id(reqhandler3),' 4:',reqhandler3,id(reqhandler5),' 5:',reqhandler5,id(reqhandler5))
print('=====')

map2 = URLMap(
  ('^/?$',reqhandler4),
  ('^/cherry/?(\w*)$',reqhandler5)
)

map1 = URLMap(
  ('^/?$',reqhandler1),
  ('^/spam/?$',reqhandler2),
  ('^/\w+\?bar\=(\d+)\&spam=(\w+)\#([a-z]{0,3})([0-9]{0,2})$',reqhandler3),
  ('^/fr(ui)ts',map2)
)

class UrlTest(unittest.TestCase):
  def testMatching(self):
    self.assertEqual(map1.match('/')[0],reqhandler1)
    self.assertEqual(map1.match('')[0],reqhandler1)
    self.assertEqual(map1.match('/spam')[0],reqhandler2)
    self.assertEqual(map1.match('/spam/')[0],reqhandler2)
    self.assertEqual(map1.match('/foo?bar=12&spam=faking#hey')[0],reqhandler3)
    self.assertEqual(map1.match('/foo?bar=12&spam=faking#99')[0],reqhandler3)
    self.assertEqual(map1.match('/foo?bar=12&spam=faking#hey99')[0],reqhandler3)

  def testSubMapMatching(self):
    self.assertEqual(map1.match('/fruits/')[0],reqhandler4)
    self.assertEqual(map1.match('/fruits/cherry')[0],reqhandler5)

  def testArguments(self):
    self.assertEqual(map1.match('/foo?bar=12&spam=faking#hey')[1],('12','faking','hey',''))
    self.assertEqual(map1.match('/foo?bar=12&spam=faking#99')[1],('12','faking','','99'))
    self.assertEqual(map1.match('/foo?bar=12&spam=faking#hey99')[1],('12','faking','hey','99'))

  def testSubMapArguments(self):
    self.assertEqual(map1.match('/fruits/')[1],('ui',))
    self.assertEqual(map1.match('/fruits/cherry/hellyeah')[1],('ui','hellyeah'))

if __name__ == '__main__':
  unittest.main()
