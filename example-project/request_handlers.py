from dasornis.core import HttpHandler
from dasornis.forms.validators import ValidateForm
from dasornis.template import Template
from dasornis import exceptions
import queries,forms

class Homepage(HttpHandler):
  def get(self):
    self.response.write("<h1>Fruit Manager</h1>")
    self.response.write("""
      <ul>
        <li><a href="/list">List Fruits</a></li>
        <li><a href="/add">Add Fruit</a></li>
        <li><a href='404'>404 page</a></li>
      </ul>
    """)

class ListPage(HttpHandler):
  def get(self):
    fruits = queries.GetFruits()
    fruits_html = '<br />'.join([ fruit[1] for fruit in fruits ])
    self.template = Template(self,'templates/list.html','pythonstring')
    self.template.args.append( ('fruits',fruits_html)  )

class AddPage(HttpHandler):
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