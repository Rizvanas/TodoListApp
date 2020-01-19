# services/users/project/config.py

import os


class Config:
    '''Base Configuration'''
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'


class DevelopmentConfig(Config):
    '''Development Configuration'''
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class TestingConfig(Config):
    '''Testing Configuration'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')


class ProductionConfig(Config):
    '''Production Configuration'''
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
