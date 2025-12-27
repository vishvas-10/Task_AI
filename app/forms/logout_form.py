from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired

class Logout_Form(FlaskForm):
    submit = SubmitField("Logout ⏻", validators=[DataRequired()])
