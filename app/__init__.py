from flask import Flask
from .models.models import db
from flask_login import LoginManager
from .routes.chart import chart_bp
from .routes.main import main_bp 
from .routes.leagues import leagues_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(main_bp)   # ← Register main blueprint for "/"
    app.register_blueprint(chart_bp)
    app.register_blueprint(leagues_bp) 

    # Set up Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

