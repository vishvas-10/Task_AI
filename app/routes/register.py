from flask import Blueprint, render_template,flash, redirect,url_for
from app.forms.register_form import Register_form
from app import db
from app.models import User,Stats
from werkzeug.security import generate_password_hash, check_password_hash

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods = ["GET","POST"])
def register():
    form = Register_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash("Email already exists!","fail")
            return redirect(url_for('auth.login'))
        first_name = form.name.data.split()[0]
        initials = "".join([word[0].upper() for word in form.name.data.split()])
        password_hash = generate_password_hash(form.password.data)
        new_user = User(name = form.name.data, email = form.email.data, password = password_hash, first_name = first_name, initials = initials)
        db.session.add(new_user)
        db.session.commit()
        flash("User created successfully!", "success")
        return redirect(url_for('auth.login'))
    return render_template('register.html', form = form)
