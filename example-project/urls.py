from dasornis.core import URLMap,StaticContent
from static.urls import map as static_urls

import request_handlers

map = URLMap(
  ('^/?$',request_handlers.Homepage),
  ('^/list',request_handlers.ListPage),
  ('^/add',request_handlers.AddPage),
  ('^/logo',StaticContent('static/logo.gif')),
  ('^/static/(.+)',static_urls)
)
