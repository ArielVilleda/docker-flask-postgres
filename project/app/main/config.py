import os

# basedir = os.path.abspath(os.path.dirname(__file__))
DB_SERVICE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}:{port}/{db}'.format(
    user=os.environ.get('POSTGRES_USER'),
    pw=os.environ.get('POSTGRES_PASSWORD'),
    url=os.environ.get('POSTGRES_SERVICE'),
    port=os.environ.get('POSTGRES_PORT', 5432),
    db=os.environ.get('POSTGRES_DB'),
)


class Config(object):
    """This Class is used to to define important flask variables
    such as connection to database and secret key
    """
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_SERVICE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = DB_SERVICE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DB_SERVICE_URI


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
key = Config.SECRET_KEY
