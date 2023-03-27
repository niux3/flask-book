from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config, basedir


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # db
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db, directory=basedir/'app'/'migrations')

    # views
    from app.main.errors import page_not_found, internal_server_error
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    from app.pages import bp as pages_views
    app.register_blueprint(pages_views)

    return app
