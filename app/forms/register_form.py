from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired, Email, Length,EqualTo

class Register_form(FlaskForm):
    name = StringField('Name', validators= [DataRequired()])
    email = StringField('Email', validators=  [DataRequired(),Email()])
    password = PasswordField('Password', validators= [DataRequired(),Length(min=8,max=20, message="Password minimum length should be 3 letters."),  EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')