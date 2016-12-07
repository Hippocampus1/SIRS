# !/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from workstation.config import WorkstationConfig as config
from workstation.decorators import try_except
from utils import logger, BaseCommand


class ListUsersCommand(BaseCommand):

    @try_except
    def do_list_users(self, input_string):
        self.setup_argparse()
        # validate arguments
        try: args = self.parser.parse_args(input_string)
        except ValueError: return
        # login user
        logger.debug("List all users")

        response = requests.get(config.CS_LIST_USERS_URL)
        response = response.json()
        if response.get("error"):
            logger.error("Error: {}".format(response.get("error")))
            return
        for object in response.get("objects"):
            logger.debug("{}".format(object))


    def help_list_users(self):
        logger.info("")