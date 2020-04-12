# -*- coding: utf-8 -*-
# Python
from datetime import timedelta
from os import getenv


class Config:
    SECRET_KEY = getenv("SECRET_KEY") or "hard to guess string"
    APP_PORT = getenv("PORT")
    DEBUG = getenv("DEBUG") or False
    SENTRY_DSN = getenv("SENTRY_DSN")
    MONGODB_HOST = getenv("MONGODB_URI")
    MONGODB_HOST_TEST = getenv("MONGODB_HOST_TEST")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SENTRY_DSN = getenv("SENTRY_DSN") or ""
    SSL_REDIRECT = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=int(getenv("JWT_ACCESS_TOKEN_EXPIRES", 20))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(getenv("JWT_REFRESH_TOKEN_EXPIRES", 30))
    )
    ENABLE_CACHE = getenv("ENABLE_CACHE") or False
    CACHE_TYPE = getenv("CACHE_TYPE", "simple")
    CACHE_REDIS_URL = getenv("CACHE_REDIS_URL")


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    USE_MOCK_DATA = True


class TestingConfig(Config):
    FLASK_ENV = "testing"
    TESTING = True
    MONGODB_HOST = getenv("MONGODB_HOST_TEST")
    SSL_REDIRECT = False
    ENABLE_CACHE = False


class ProductionConfig(Config):
    DEBUG = False


class QaConfig(ProductionConfig):
    DEBUG = False


class HerokuConfig(ProductionConfig):
    SSL_REDIRECT = True if getenv("DYNO") else False


class DockerConfig(ProductionConfig):
    pass


class UnixConfig(ProductionConfig):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "qa": QaConfig,
    "production": ProductionConfig,
    "heroku": HerokuConfig,
    "docker": DockerConfig,
    "unix": UnixConfig,
    "default": DevelopmentConfig,
}
