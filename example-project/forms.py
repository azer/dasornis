from dasornis.forms import Form, Textbox
import patterns

class NewFruit(Form):
    fruit_name = Textbox(name='fruit',label_i18n_key='fruit_name',is_required=True,min_length=3,max_length=10,pattern=patterns.safe_text)
