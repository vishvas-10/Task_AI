from flask import Blueprint,render_template,session,flash,redirect,url_for
from app.models import User
from app.decorators import is_authenticated
from app.forms.logout_form import Logout_Form
from app.forms.password_form import PasswordForm
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

profile_bp = Blueprint('profile',__name__)


@profile_bp.route('/profile')
@is_authenticated
def profile():
    form = Logout_Form()
    current_user = session['user']
    current_user = User.query.get(current_user)
    return render_template('profile.html', user = current_user, form = form)

@profile_bp.route('/change-password', methods = ["POST","GET"])
@is_authenticated
def change_password():
    form = PasswordForm()
    if form.validate_on_submit():
        curr_user = User.query.get(session['user'])
        if check_password_hash(curr_user.password, form.old_password.data):
            curr_user.password = generate_password_hash(form.new_password.data)
            db.session.commit()
            session.clear()
            flash('Password changed succeffully!','success')
            return redirect(url_for('auth.login'))
        else:
            flash('Old Password Did Not Match!','fail')
            return redirect(url_for('profile.change_password'))
    else:
        return render_template('change_password.html', form = form)