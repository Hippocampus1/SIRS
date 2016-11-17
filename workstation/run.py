import sys
import argparse
import requests
from config import WorkstationConfig as config
from utils import logger as log


def login_user(username, password):
    """"""
    response = None
    try:
        response = requests.post(config.CS_LOGIN_URL, json={"username": username, "password": password})
        response = response.json()
        if response.get("error"):
            log.error("Error: {}".format(response.get("error")))
            sys.exit(1)

    except Exception, e:
        log.error(e)
        log.warning("Central Server is unreachable. Try again later")
        sys.exit(1)

if __name__ == "__main__":
    log.info("Starting workstation...")
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', dest='username', type=str, default=None, help='User username.', required=True)
    parser.add_argument('-p', dest='password', type=str, default=None, help='User password.', required=True)
    # validate arguments
    args = parser.parse_args()
    log.debug("User \"{}:{}\" is trying to login...".format(args.username, args.password))
    # login user
    user = login_user(args.username, args.password)

    sys.exit(1)

    # print confirmation an display menu
    log.info("Valid Credentials. Welcome!")
    try:
        while(True):
            # waits for client input:
            input_data = raw_input()
            # handle which command should run
            if input_data.startswith('lol'):
               pass
            elif input_data == 'help':
                # help - show list of possible commands
                commands = map(lambda x: '\t> {}'.format(x), [
                    'list: Requesting list of possible translations from TCS server.',
                    'request: Requesting translation for given arguments.\n\t\t> request n t N W1 W2 ... WN\n\t\t> request n f filename',
                    'exit: Exit current user application.',
                ])
                log.info("""List of possible commands:\n{}""".format(
                    "\n".join(commands)))
            else:
                # validate corner cases
                if input_data.strip() != '':
                    log.warning("\"{}\" command does not exist.".format(input_data))
    except KeyboardInterrupt, e:
        # if CTRL+C is pressed, then go for last step
        log.info("\nCTRL+C - Exiting user application.")
        pass
    log.info("Cya next time :)!")
    sys.exit(1)
