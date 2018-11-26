# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from collector.config import config


def create_app(settings_override={}):
    app = Flask(__name__)

    app_env = os.getenv('FLASK_ENV', 'default')

    app.config.from_object(config[app_env])

    db.init_app(app)

    from collector.views.user import user
    app.register_blueprint(user)

    from collector.views.location import location
    app.register_blueprint(location)

    from collector.views.collector import collector
    app.register_blueprint(collector)

    from collector.views.category import category
    app.register_blueprint(category)

    from collector.views.collection import collection
    app.register_blueprint(collection)

    from collector.views.request import request
    app.register_blueprint(request)

    return app


ma = Marshmallow(create_app)
db = SQLAlchemy()
