from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix
load_dotenv()

#create a database object not yet connected
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )
    app.config['SECRET_KEY'] =os.getenv('SECRET_KEY')
    app.config['SESSION_COOKIE_HTTPONLY']=True
    is_prod = os.environ.get('FLASK_ENV') == 'production'
    app.config['SESSION_COOKIE_SECURE']=is_prod   
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    csrf = CSRFProtect(app)
    app.config['SESSION_PERMANENT'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
    "pool_recycle": 300,  # 5 minutes
}

    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.home import home_bp
    from app.routes.tasks import tasks_bp
    from app.routes.register import register_bp
    from app.routes.profile import profile_bp
    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(dashboard_bp)

    with app.app_context():
        # Important: Import models here so SQLAlchemy knows what tables to create
        from app import models 
        db.create_all()

    return app
