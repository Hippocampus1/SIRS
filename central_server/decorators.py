# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 12/7/16"""
from functools import wraps
from flask_login import current_user
from flask import request, redirect, url_for
from utils import logger as log

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            message = "User needs to be logged in to access this resource!"
            log.error(message)
            return redirect(url_for('error_view', message=message))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.is_admin:
            message = "User needs to be an admin to access this resource!"
            log.error(message)
            return redirect(url_for('error_view', message=message))
        return f(*args, **kwargs)
    return decorated_function