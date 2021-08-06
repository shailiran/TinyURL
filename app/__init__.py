from flask import Flask
from flask_migrate import Migrate

from .extensions import db
from .routes import short

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    if type(config_name) is not dict:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(config_name)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(short)

    from app import models
    with app.app_context():
        db.create_all()
        db.session.commit()
        
    migrate = Migrate(app, db)

    return app
