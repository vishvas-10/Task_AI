from functools import wraps
from flask import g, redirect, url_for, flash, session

def is_authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Assuming you are using Flask-Login, check if user is logged in
        if session.get('user'):
            return f(*args, **kwargs)
        else:
            flash('Please log in to access this page.', 'fail')
            return redirect(url_for('auth.login')) # Adjust to your login route
    return decorated_function
