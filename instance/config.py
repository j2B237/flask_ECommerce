""" Application configuration module """
import os


class Config:
    SECRET_KEY = os.urandom(16)


class DevelopmentConfig(Config):
    """ Development configuration inherits from base config """
    ENV = "development"
    DEBUG = True


class ProductionConfig(Config):
    """ Production configuration inherits from base config """
    ENV = "production"
    DEBUG = False


class TestingConfig(Config):
    """ Testing configuration inherits from base config """
    ENV = "test"


config = {
    "default": DevelopmentConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}