from flask import Flask
from flask_uploads import configure_uploads

from store.extensions import *
from store.admin import create_admin
from store.config import config


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    # Init extensions
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app)
    api.init_app(app)
    cors.init_app(app)

    configure_uploads(app, images)

    from store.core.helper import auto_import_model, auto_import_controller

    # auto imports
    auto_import_model()
    auto_import_controller()

    create_admin()

    return app
