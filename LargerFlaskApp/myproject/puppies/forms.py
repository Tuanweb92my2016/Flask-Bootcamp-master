#forms.py puppies

from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy : ')
    submit = SubmitField('Add Puppy ')

class DelForm(FlaskForm):

    id = IntegerField("Id Number of Puppy to remove : ")
    submit = SubmitField("Remove puppy ")
