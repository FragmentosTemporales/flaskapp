import os
from datetime import timedelta
from config import settings as s


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """ Base configuration application class """
    JWT_SECRET_KEY = s.jwt_secret_key
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=int(s.jwt_access_token_expires_hours)
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(s.jwt_access_token_expires_days)
    )
    SECRET_KEY = s.secret_key


class DevConfig(BaseConfig):
    """ Development configuration class """
    db_user = s.postgres_user
    db_pass = s.postgres_password
    db_name = s.postgres_db
    db_host = s.postgres_host
    db_port = s.postgres_port
    SQLALCHEMY_DATABASE_URI = ("postgresql://{}:{}@{}:{}/{}".format(
        db_user, db_pass, db_host, db_port, db_name
    ))


class TestConfig(BaseConfig):
    """ Testing configuration class """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, "..", 'test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "dev": DevConfig,
    "test": TestConfig
    }