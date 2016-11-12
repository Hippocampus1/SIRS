#!/usr/bin/python

import settings
from utils import logger as log

import mysql.connector
from mysql.connector import errorcode


try:
    log.debug("Connecting to mysql DB with config:({}).".format(settings.DB_CONFIG))
    cnx = mysql.connector.connect(**settings.DB_CONFIG)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        log.error("Mysql given Database does not exist.")
    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        log.error("Username and Password don't exist.")
    else:
        log.error("Unexpected error when trying to connect with Mysql Database.")
else:
    log.debug("Closing connection to mysql db")
    cnx.close()
