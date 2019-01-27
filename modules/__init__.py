##
##
##
##
##

## Imports

from .set import AttackWindow
from ..core.windows import OptionWindow

##

class MainWindow(OptionWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_option("Social-Engineering Attacks", self.sub_to_attacks)
        self.add_option("Penetration Testing (Fast-Track)", self.sub_to_pentest)
        self.add_option("Third Party Modules", self.sub_to_thirdparty)
        self.add_option("Update the Social-Engineer Toolkit", self.sub_to_update)
        self.add_option("Update SET configuration", self.sub_to_config)
        self.add_option("Help, Credits, and About", self.sub_to_help)

    def sub_to_attacks(self, *args, **kwargs):
        attack_menu = AttackWindow("SE Toolkit - Attacks", self)
        attack_menu.display_options()

    def sub_to_pentest(self, *args, **kwargs):
        print("Test 2")

    def sub_to_thirdparty(self, *args, **kwargs):
        print("Test 3")

    def sub_to_update(self, *args, **kwargs):
        print("Test 4")

    def sub_to_config(self, *args, **kwargs):
        print("Test 5")

    def sub_to_help(self, *args, **kwargs):
        print("Test 6")

##

main_menu = MainWindow("SE Toolkit", None)
main_menu.display_options()