import os


class Config(object):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    TESTING = False
    CORS_HEADERS = 'Content-Type'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_IMAGES_DEST = imagedir = 'static/images'
    UPLOADED_IMAGES_URL = '/static/images/'


class DevelopmentConfig(Config):
    SECRET_KEY = 'dev-secret'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/store_api'


class ProductionConfig(Config):
    SECRET_KEY = 'prod-secret'


config = DevelopmentConfig() if os.environ.get('FLASK_ENV') == 'development' else ProductionConfig()
