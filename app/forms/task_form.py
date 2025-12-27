from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length

class Task_Form(FlaskForm):
    task = StringField('Task Name',validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Add Task')