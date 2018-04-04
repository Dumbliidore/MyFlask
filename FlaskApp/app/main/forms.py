# -*-coding:utf-8-*-

__Author__ = "Mr.D"
__Date__ = '2018\4\1 0001 22:30'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')