from flask_wtf import Form
from wtforms import StringField, BooleanField,  TextAreaField, SelectMultipleField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from datetime import datetime





class TaskForm(Form):
    task_name = StringField('task_name', validators=[DataRequired()])
    content = StringField('content', validators=[DataRequired()])
    expire_date = StringField('expire_date', validators=[DataRequired()])
    principal = StringField('principal', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
