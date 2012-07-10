import unittest,sys,os.path
sys.path.append(os.path.dirname(__file__)+'../')
from dasornis.db import Entity
from dasornis.db import Query
from dasornis.db import Field
from dasornis.log import logging
from pdb import set_trace

class Author(Entity):
  id = Field()
  name = Field()
  bar = Field()

class GetAuthor(Query):
  code = "SELECT 314,'azer koculu',%i"
  entity = Author
  is_singular = True
  
class Book(Entity):
  id = Field()
  name = Field()
  author = Field(filter=GetAuthor)
  foo = Field()

class GetBook(Query):
  code = "SELECT 108,'alice in wonderland',314,%i"
  entity = Book
  is_singular = True

class GetBook2(Query):
  code = "SELECT 108,'alice in wonderland',1,%(foo)d"
  entity = Book
  is_singular = True


class GetBooks(Query):
  code = "SELECT 108,'azer in wonderland',314"
  entity = Book

class Test(unittest.TestCase):
  def testSingularFetching(self):
    book = GetBook(666)
    self.assertEqual(isinstance(book,Book),True)
    self.assertEqual(book.id,108)
    self.assertEqual(book.name,'alice in wonderland')
    self.assertEqual(book.author.name,'azer koculu')
    self.assertEqual(book.author.bar,314)
    
    book2 = GetBook2(foo=666)
    self.assertEqual(book.foo,666)

  def testPluralFetching(self):
    books = GetBooks()
    self.assertEqual(isinstance(books[0],Book),True)
    self.assertEqual(isinstance(books[0].author,Author),True)
    self.assertEqual(books[0].author.id,314)
    self.assertEqual(books[0].author.name,'azer koculu')

    for book in books:
      self.assertEqual(isinstance(book,Book),True)

  def testType(self):
    class Crap(Entity):
      fu = Field(type=int)

    class GetCrap(Query):
      code = 'select NULL'
      entity = Crap
      is_singular = True
      
    try:
      crap = GetCrap()
    except TypeError:
      self.assertEqual(1,1)
    else:
      self.assertEqual(0,1)

if __name__ == '__main__':
  unittest.main()
