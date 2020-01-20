# services/users/project/config.py

import os


class Config:
    '''Base Configuration'''
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'
    BCRYPT_LOG_ROUNDS = 13


class DevelopmentConfig(Config):
    '''Development Configuration'''
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(Config):
    '''Testing Configuration'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')
    BCRYPT_LOG_ROUNDS = 4


class ProductionConfig(Config):
    '''Production Configuration'''
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
