# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
from workstation.config import WorkstationConfig as config
from utils import logger, BaseCommand


class LoginCommand(BaseCommand):

    def do_login(self, input_string):
        self.setup_argparse(usage="$ login -u username -p password ",
                            description='Login')
        self.parser.add_argument('-u', dest='username', type=str, default=None, help='User username.', required=True)
        self.parser.add_argument('-p', dest='password', type=str, default=None, help='User password.', required=True)
        # validate arguments
        try: args = self.parser.parse_args(input_string)
        except ValueError: return
        # login user
        logger.debug("User \"{}:{}\" is trying to login...".format(
            args.username, args.password))

        response = None
        try:
            json = {"username": args.username, "password": args.password}
            response = requests.post(config.CS_LOGIN_URL, json=json)
            response = response.json()
            if response.get("error"):
                logger.error("Error: {}".format(response.get("error")))
                sys.exit(1)
            logger.info("Valid Credentials. Welcome!")

        except Exception, e:
            logger.error(e)
            logger.warning("Central Server is unreachable. Try again later")
            sys.exit(1)

    def help_login(self):
        logger.info("Login")