Dasornis is a highly-customizable Python Web Framework that I coded on March
2009. It consists of HTTP, ORM, Templating, I18n and Form libraries.  See the example
application for details.

# Usage Example

### Defining Models

```python
# queries.py

from dasornis.db import Entity, Query, Field

class Fruit(Entity):
    id = Field()
    name = Field()

class FindFruits(Query):
    entitiy = Fruit
    code = 'SELECT id,name FROM fruits'

class CreateFruit(Query):
    code = "INSERT INTO fruits(name) VALUES ('%s')"
```

### Templates and Forms 

```python
# forms.py

from dasornis.forms import Form, Textbox

safe_text = r'[\w\s]+'

class NewFruit(Form):
  fruit_name = Textbox(name='fruit', label_i18n_key='fruit_name', is_required=True, min_length=3, max_length=10, pattern=safe_text)
```

```html
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:py="http://genshi.edgewall.org/"
      xmlns:xi="http://www.w3.org/2001/XInclude"
      py:strip='True'>
  <xi:include href="generate_form.html" />
  <head>
    <title>Add Fruit</title>
  </head>
  <body>
    <fieldset class='NewMessage'>
      <legend>Add Fruit</legend>
        Report Message: ${ i18n | report.message_key }
        <form method='POST' action='/add'>
          ${ generate_form(template.form) }
          <button>Send</button>
        </form>
    </fieldset>
  </body>
</html>
```

### HTTP

```python
# urls.py

from dasornis.core import URLMap,StaticContent
from static.urls import map as static_urls

import request_handlers

map = URLMap(
  ('^/add',request_handlers.NewFruit),
  ('^/logo',StaticContent('static/logo.gif')),
  ('^/static/(.+)',static_urls)
)
```

```python
# request_handlers.py

from dasornis.core import HttpHandler
from dasornis.forms.validators import ValidateForm
from dasornis.template import Template
from dasornis import exceptions
import queries,forms

class NewFruit(HttpHandler):
  def init(self):
    self.template = Template(self,'add.html','genshi_engine')
    self.template.form = forms.NewFruit()
    self.template.args.append( ('fields',self.template.form._fields_) )

  def post(self):
    try:
      self.save()
    except exceptions.LengthError:
      self.report.report_type = self.report.ERROR
      self.report.message_key = 'length_error'
    except exceptions.MissingInfo:
      self.report.report_type = self.report.ERROR
      self.report.message_key = 'missing_info'

  @ValidateForm()
  def save(self):
    queries.CreateFruit(self.request.POST['fruit'])
    self.redirect('/list')
```
