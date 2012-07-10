class HttpResponse:
  """
  A Basic Http Response Class for WSGI Applications
  """
  def __init__(self,content=None):
    self._content = [] if not content else [content]
    self.headers = {}
    self.status = '200 OK'

  def __iter__(self):
    return iter(self._content)

  @property
  def content(self):
    return ''.join(self._content)

  @content.setter
  def content(self,content):
    self._content = [content]

  def write(self,content):
    self._content.append(content)