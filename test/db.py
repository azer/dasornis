import unittest,sys,os.path
sys.path.append(os.path.dirname(__file__)+'../')

from dasornis.db import connection

class Test(unittest.TestCase):
  def testConnection(self):
    self.assertEqual( connection.link.status, 1 )

  def testQueryExecution(self):
    connection.cursor.execute("SELECT 10,20,30")
    data = connection.cursor.fetchall()
    self.assertEqual( data,[(10,20,30)])
  def testTransactions(self):
    try:
      connection.cursor.execute("SPAM;")
    except: pass

    connection.cursor.execute("SELECT 666")
    self.assertEqual(connection.cursor.fetchone()[0],666)

if __name__ == '__main__':
  unittest.main()
