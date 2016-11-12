# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Global Settings file"""
import os

# Group Number
GN = 53

# Set logging level as debug
DEBUG = True

# Configuration for MySql database connection
# (source: https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)
DB_CONFIG = {
  'user': 'scott',
  'password': 'tiger',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True,
}
