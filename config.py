class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/joke_api"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/joke_api_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {"development": DevelopmentConfig, "test": TestConfig}
