from dasornis.log import logging

class DBConnection(object):
  def __init__(self,**kwargs):
    self._link = None
    self._cursor = None

    self.driver = kwargs.get('driver')
    self.user = kwargs.get('user')
    self.password = kwargs.get('password')
    self.host = kwargs.get('host')
    self.database = kwargs.get('database')

  def open(self,**kwargs):
    logging.info("db: Initializing new connection..")
    self._link = self.driver.connect(
      user = self.user,
      password = self.password,
      host = self.host,
      database = self.database
    )
    self._cursor = None

  @property
  def link(self):
    if not self._link:
      self.open()
    return self._link

  @link.setter
  def link(self,value):
    raise AssertionError("Connection property is read-only.")
  
  @property
  def cursor(self):
    if self._link and self._link.get_transaction_status()==3:
      logging.warning("db: Transaction is corrupted")
      logging.info("db: Running rollback command")
      self._link.rollback()

    if not self._cursor:
      logging.info("db: Initializing new database cursor.")
      self._cursor = self.link.cursor()

    return self._cursor

  @cursor.setter
  def cursor(self):
    raise AssertionError("Cursor property is read-only")
