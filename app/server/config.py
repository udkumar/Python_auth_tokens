import os

basedir = os.path.abspath(os.path.dirname(__file__))

# PostgreSQL
host = os.environ.get("AUTH_POSTGRES_HOST","localhost")
port = os.environ.get("AUTH_POSTGRES_PORT", "5432")
username = os.environ.get("AUTH_POSTGRES_USER", "amt")
password = os.environ.get("AUTH_POSTGRES_PASSWORD", "mt2414@123")
database = os.environ.get("AUTH_POSTGRES_DATABASE", "python_auth_tokens")

postgres_local_base = 'postgresql://{username}:{password}@{host}:{port}/'.format(username=username, password=password, host=host, port=port)


class BaseConfig:
    '''Base configuration.'''
    SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET_KEY')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    '''Development configuration.'''
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database


class TestingConfig(BaseConfig):
    '''Testing configuration.'''
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    '''Production configuration.'''
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///example'