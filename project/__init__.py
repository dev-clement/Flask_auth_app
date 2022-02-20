from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkeygoeshere'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db.sqlite'

    db.init_app(app)

    # Blueprint for auth route
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth part of the app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app