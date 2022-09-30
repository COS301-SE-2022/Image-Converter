from database.database import User
from database.mockDatabase import mockDatabase

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY='secret'
    DB_NAME='REAL'
    DATABASE=User()

class TestingConfig(Config):
    DB_NAME='Mock'
    DATABASE=User()