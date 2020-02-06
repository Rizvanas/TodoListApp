# services/users/project/config.py

import os


class Config:
    '''Base Configuration'''
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    BCRYPT_LOG_ROUNDS = 13
    TOKEN_EXPIRATION_DAYS = 30
    TOKEN_EXPIRATION_SECONDS = 0
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


class DevelopmentConfig(Config):
    '''Development Configuration'''
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(Config):
    '''Testing Configuration'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRATION_DAYS = 0
    TOKEN_EXPIRATION_SECONDS = 3


class ProductionConfig(Config):
    '''Production Configuration'''
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
