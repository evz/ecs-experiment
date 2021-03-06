from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from .views import views
from .database import db

def create_app(name=__name__, settings_override={}):
    app = Flask(name)
    config = '{0}.app_config'.format(__name__)
    app.config.from_envvar('APPLICATION_CONFIG')
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DB_CONN']

    for k,v in settings_override.items():
        app.config[k] = v

    db.init_app(app)

    with app.test_request_context():
        db.create_all()

    app.register_blueprint(views)

    return app
