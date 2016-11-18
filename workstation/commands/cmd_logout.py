# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
from workstation.config import WorkstationConfig as config
from utils import logger, BaseCommand


class LogoutCommand(BaseCommand):

    def do_logout(self, input_string):
        self.setup_argparse(
            usage="$ logout",
            description='Logout current logged in user')
        # validate arguments
        try: args = self.parser.parse_args(input_string)
        except ValueError: return

        # logging out user
        response = requests.post(config.CS_LOGOUT_URL, json={})


    def help_logout(self):
        logger.info("Terminates current session for logged user.")