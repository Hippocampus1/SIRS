# !/usr/bin/python
# -*- coding: utf-8 -*-
from utils import logger, BaseCommand


class CreateUserCommand(BaseCommand):



    def do_create_user(self, input_string):
        self.setup_argparse(
            usage="$ create-user -u username -p password -t user_type "
                  "[first_name] [last_name] [email]",
            description='Create user with given arguments')
        self.parser.add_argument('-u',
            dest='username', type=str, default=None,
            help='User username.', required=True)
        self.parser.add_argument('-p',
            dest='password', type=str, default=None,
            help='User password.', required=True)
        self.parser.add_argument('-t',
            dest='user_type', type=str, default=None,
            help='User type.', required=True)
        # validate arguments
        try: args = self.parser.parse_args(input_string)
        except ValueError: return

        logger.info("Creating user with {}".format(args))


    def help_create_user(self):
        logger.info("Create user with given arguments")
