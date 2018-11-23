# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


def create_app():
    app = Flask(__name__)

    app.config.from_object('collector.config.Config')

    db.init_app(app)

    from collector.views.user import user
    app.register_blueprint(user)

    return app


ma = Marshmallow(create_app)
db = SQLAlchemy()
