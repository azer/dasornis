from dasornis.core import URLMap,StaticContent

map = URLMap(
  ('(.+)',StaticContent('static/'))
)
