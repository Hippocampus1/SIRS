# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Workstating Settings file"""
from global_config import BaseConfig


class WorkstationConfig(BaseConfig):
    CS_HOST_URL = "http://127.0.0.1:5000/"

    CS_LOGIN_URL = CS_HOST_URL + "login/"
    CS_LOGOUT_URL = CS_HOST_URL + "logout/"

    CS_CREATE_USER_URL = CS_HOST_URL + "create-user/"
    CS_UPDATE_USER_URL = CS_HOST_URL + "update-user/"
    CS_DELETE_USER_URL = CS_HOST_URL + "delete-user/"

    CS_LIST_USERS_URL = CS_HOST_URL + "list-users/"

__all__ = ['WorkstationConfig']
