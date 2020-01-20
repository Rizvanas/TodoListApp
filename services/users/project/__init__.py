# services/users/project/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
cors = CORS()
bcrypt = Bcrypt()


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
