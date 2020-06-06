import os

DATABASE_DEFAULT = "postgresql://localhost/joke_api"


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", DATABASE_DEFAULT)


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/joke_api_test"


config = {"development": DevelopmentConfig, "test": TestingConfig}
