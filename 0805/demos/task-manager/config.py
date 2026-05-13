import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DATABASE = os.environ.get("DATABASE", os.path.join(BASE_DIR, "taskflow.db"))
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DATABASE = os.path.join(BASE_DIR, "test.db")


class ProductionConfig(Config):
    SECRET_KEY = os.environ["SECRET_KEY"]  # must be set explicitly in production
    DATABASE = os.environ.get("DATABASE", os.path.join(BASE_DIR, "taskflow.db"))


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}


def get_config():
    env = os.environ.get("FLASK_ENV", "default")
    return config.get(env, config["default"])
