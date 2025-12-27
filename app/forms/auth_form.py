from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired, Email, Length

class Login_form(FlaskForm):
    email = StringField('Email', validators=  [DataRequired(),Email()])
    password = PasswordField('Password', validators= [DataRequired(),Length(min=8, message="Password minimum length should be 3 letters.",max=18)])
    submit = SubmitField('Sign In')