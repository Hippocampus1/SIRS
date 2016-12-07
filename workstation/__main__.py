import sys
from utils import logger as log, BaseMenu
from workstation.commands import *
from workstation.exceptions import *

# import and create WorkstationMenu with all available commands
class AnnonymousWorkstationMenu(BaseMenu,
                                LoginCommand):
    pass


class PacientWorkstationMenu(AnnonymousWorkstationMenu,
                             ListUsersCommand,
                             LogoutCommand):
    intro = "=== Pacient Medical Workstation ==="
    pass


class AdminWorkstationMenu(PacientWorkstationMenu, CreateUserCommand):
    intro = "=== Admin Medical Workstation ==="
    pass


log.info("Starting workstation...")
try:
    AnnonymousWorkstationMenu().cmdloop()
except PacientLevelUp, e:
    log.info("Pacient Priviledge Mode")
    PacientWorkstationMenu().cmdloop()
except AdminLevelUp, e:
    log.info("Admin Priviledge Mode")
    AdminWorkstationMenu().cmdloop()
except KeyboardInterrupt, e:
    # if CTRL+C is pressed, then go for last step
    log.info("CTRL+C - Exiting user application.")
    pass

log.info("Cya next time :)!")
sys.exit(1)

