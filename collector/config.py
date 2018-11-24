# -*- coding: utf-8 -*-
import os


class Config(object):
    DEBUG = True if os.environ.get('DEBUG', None) else False
    SQLALCHEMY_DATABASE_URI = 'mysql://dumny:dumny@db/ereciclar'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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
