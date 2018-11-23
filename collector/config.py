# -*- coding: utf-8 -*-
import os


class Config(object):
    DEBUG = True if os.environ.get('DEBUG', None) else False

    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_DATABASE_URI = 'mysql://dumny:dumny@db/ereciclar'


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
