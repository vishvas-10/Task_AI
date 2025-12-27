from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired, Email, Length,EqualTo


class PasswordForm(FlaskForm):
    old_password=PasswordField('Old Password', validators=[DataRequired()])
    new_password=PasswordField('New Password', validators=[DataRequired(),Length(min=8,max=18),EqualTo('confirm_password')])
    confirm_password=PasswordField('Confirm Password', validators=[DataRequired()])
    submit=SubmitField('Change Password')