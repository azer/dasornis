from dasornis import config
from dbconnection import DBConnection
from entity import Entity
from field import Field
from query import Query

connection = DBConnection(
  driver = config.DB_DRIVER,
  user = config.DB_USER,
  password = config.DB_PASSWORD,
  host = config.DB_HOST,
  database = config.DB_NAME
)

