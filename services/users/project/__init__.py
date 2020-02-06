# services/users/project/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
cors = CORS()
bcrypt = Bcrypt()
jwt = JWTManager()

blacklist = set()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    from project.api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
