# !/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
from workstation.config import WorkstationConfig as config
from workstation.decorators import try_except
from utils import logger, BaseCommand


class LogoutCommand(BaseCommand):

    @try_except
    def do_logout(self, input_string):
        self.setup_argparse(
            usage="$ logout",
            description='Logout current logged in user')
        # validate arguments
        try: args = self.parser.parse_args(input_string)
        except ValueError: return

        # logging out user
        response = requests.post(config.CS_LOGOUT_URL, json={})
        response = response.json()
        if response.get("error"):
            logger.error("Error: {}".format(response.get("error")))
            return
        logger.info("Cya :)")


    def help_logout(self):
        logger.info("Terminates current session for logged user.")