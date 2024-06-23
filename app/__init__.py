import os
from flask import Flask, render_template
from app.config import config
from app.models import db, migrate
from app.routes.main import jwt, cors, main
from config import settings as s

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app(test_mode=False):
    app = Flask(__name__, instance_relative_config=True)

    if test_mode:
        app.config.from_object(config["test"])
    else:
        env = s.flask_env
        app.config.from_object(config[env])

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    app.register_blueprint(main)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error_404.html'), 404

    return app