import sys
from utils import logger as log, BaseMenu
from workstation.commands import (LoginCommand, LogoutCommand,
                                  CreateUserCommand)

# import and create WorkstationMenu with all available commands
class WorkstationMenu(BaseMenu,
                      LoginCommand,
                      LogoutCommand,
                      CreateUserCommand):
    pass

if __name__ == "__main__":
    log.info("Starting workstation...")
    try:
        WorkstationMenu().cmdloop()
    except KeyboardInterrupt, e:
        # if CTRL+C is pressed, then go for last step
        log.info("CTRL+C - Exiting user application.")
        pass
    log.info("Cya next time :)!")
    sys.exit(1)

