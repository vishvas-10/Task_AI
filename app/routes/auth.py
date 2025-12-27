from flask import Blueprint, render_template, session, flash, redirect, url_for
from app.forms.auth_form import Login_form
from app import db
from app.models import User
from app.decorators import is_authenticated
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods = ["GET","POST"])
def login():
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                session['user'] = user.id
                return redirect (url_for('dashboard.dashboard'))
            else:
                flash("Invalid Login Credentials!","fail")
                return redirect (url_for('auth.login'))
        else:
            flash("Email does not exist! Try Signing Up.","fail")
            return redirect (url_for('auth.login'))

    else:
        return render_template('login.html', form = form)
    

@auth_bp.route('/logout', methods = ["GET","POST"])
@is_authenticated
def logout():
    session.clear()
    return redirect(url_for('home.home'))