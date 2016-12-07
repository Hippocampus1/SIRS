# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import cmd
import argparse
from global_config import BaseConfig


class Logger(object):
    """Utils Logging has 4 variables that controls if the log goes to the output(screen)
    _error, _debug, _warning and _info default:  all loggers are enable except debug, which is False

    to enable debug log just add the following lines to your code:

    from utils import Logger
    log = Logger(debug=True)
    log.info("Information message")
    """
    def __init__(self, debug=False, info=True, error=True, warning=True):
        self._error = error
        self._debug = debug
        self._warning = warning
        self._info = info

    def error(self, msg):
        if self._error:
            print("[ERROR]: {}".format(msg))

    def debug(self, msg):
        if self._debug:
            print("[DEBUG]: {}".format(msg))

    def info(self, msg):
        if self._info:
            print("[INFO]: {}".format(msg))

    def warning(self, msg):
        if self._warning:
            print("[WARNING]: {}".format(msg))

logger = Logger(debug=BaseConfig.DEBUG)


class BaseMenu(cmd.Cmd):
    """"""
    prompt = '$ '
    intro = "=== Medical Workstation ==="

    doc_header = 'Documented commands: "$ help <command>"'
    misc_header = ''
    undoc_header = ''
    ruler = '-'

    context = {}

    def do_exit(self, string_input):
        logger.debug("Exiting application")
        return True

    def help_exit(self):
        logger.info("Exit current user application.")


class BaseCommand(object):
    """Abstraction for each of our custom commands"""

    context = {}

    def __init__(self, *args, **kwargs):
        super(BaseCommand, self).__init__(*args, **kwargs)

    def setup_argparse(self, **kwargs):
        """Wrapper that returns custom ArgumentParser object"""
        class CustomArgumentParser(argparse.ArgumentParser):
            """Custom ArgumentParser for BaseMenu"""
            def parse_args(self, args=None, namespace=None):
                # make sure input arguments are a list and not a string
                args = args.split()
                args = super(CustomArgumentParser, self).parse_args(
                    args, namespace)
                if getattr(self, "trigger_error_exception", False):
                    raise ValueError("CustomArgumentParser Error:")
                return args

            def error(self, message):
                """overwrites error ArgumentParser method so it doesnt
                call exit function"""
                self._print_message('[ERROR]: %s\n' % message, sys.stderr)
                self.trigger_error_exception = True

        self.parser = CustomArgumentParser(**kwargs)
        return self.parser

__all__ = ['logger', "BaseMenu", "BaseCommand"]
