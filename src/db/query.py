from query_result import QueryResult
from dasornis.log import logging
from dasornis.lib.exception_info import ExceptionInfo

class Query(object):
  args = None
  code = None
  entity = None
  data = None
  is_singular = False

  def __call__(self,*args,**kwargs):
    """
    Handles calling event of the classes.Executes given query using database driver.
    Returns instances of Entity classes which will be mapped to sub query classes.
    """
    self.args = args or kwargs or None
    if not self.code:
      raise Exception, "'code' property has to be an sql query"

    if self.args:
      code = self.code%self.args
    else:
      code = self.code

    logging.info('db.query: Running new query; %s'%(code.replace('\n',' ')))
    """
    Executing given query
    """
    from __init__ import connection
    connection.cursor.execute(code)

    try:
      data = connection.cursor.fetchall()
    except:
      data = tuple()
      logging.error( ExceptionInfo().format_stack() )

    """
    Mapping fetched data into python objects
    """
    self.data = QueryResult(data)
    self.data.query = self
    self.data = ( None if len(self.data)==0 else self.data[0] ) if self.is_singular else self.data

    return self.data

  def __new__(cls,*args,**kwargs):
    return object.__new__(cls)(*args,**kwargs)
