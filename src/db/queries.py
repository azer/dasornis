from query import Query

class Commit(Query):
  code = "COMMIT"

class Rollback(Query):
  code = "ROLLBACK"
