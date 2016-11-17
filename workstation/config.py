# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Workstating Settings file"""
from global_config import BaseConfig

class WorkstationConfig(BaseConfig):
    CS_LOGIN_URL = "http://127.0.0.1:5000/login/"


__all__ = ['WorkstationConfig']
