# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Global Settings file"""
import os

class BaseConfig(object):
    # Environment
    # APP_ENV = "localhost"

    # Debug and testing.
    DEBUG = True

    # Group Number
    GN = 53

    # DB Configuration
    DB_USER = 'sql8144902'
    DB_PASSWORD ='U4P8dsfUBr'
    DB_HOST = 'sql8.freemysqlhosting.net'
    DB_DATABASE = 'sql8144902'

    SECRET_KEY = os.environ.get("SECRET_KEY", "THISSHOULDBEKEPTSECRET")
    # WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = True


__all__ = ['BaseConfig']
