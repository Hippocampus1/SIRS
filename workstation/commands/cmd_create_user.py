# !/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from workstation.config import WorkstationConfig as config
from utils import logger, BaseCommand
from workstation.decorators import try_except


class CreateUserCommand(BaseCommand):

    @try_except
    def do_create_user(self, input_string):
        self.setup_argparse()
        self.parser.add_argument('-u',
            dest='username', type=str, help='User username.', required=True)
        self.parser.add_argument('-p',
            dest='password', type=str, help='User password.', required=True)
        # validate arguments
        try: args = self.parser.parse_args(input_string)
        except ValueError: return
        # populate optional fields
        logger.info("Please, fill the following optional fields:")
        fields = ['first_name', 'last_name', 'email']
        optional_args = dict(zip(fields, [None] * len(fields)))
        for field_name in fields:
            field_value = raw_input("{}: ".format(field_name))
            optional_args.setdefault(field_name, field_value)

        logger.info("Creating user with {} and {}".format(args, optional_args))
        json = {
            "username": args.username, "password": args.password
        }
        json.update(optional_args)

        response = requests.post(config.CS_CREATE_USER_URL,
                                 headers=self.context.get('headers'),
                                 json=json)
        response = response.json()
        if response.get("error"):
            logger.error("Error: {}".format(response.get("error")))
            return
        logger.info(response)

    def help_create_user(self):
        logger.info("""Create user with given arguments:
    -u username: User's new username
    -p password: User's new password
    [first_name]: User's first name
    [last_name]: User's last name
    [email]: User's email

    Format: $ create-user -u username -p password -t user_type [first_name] [last_name] [email]"
""")
