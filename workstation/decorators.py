# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Created by andresilva on 12/7/16"""
from functools import wraps
from utils import logger as log


def try_except(f):
    @wraps(f)
    def prevent_fail(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception, e:
            log.error("Something went wrong with \"{}\": {}"
                      "".format(f.__name__, e))
            return None
    return prevent_fail