##
##
##
##
##

## Imports

from ..core.frame import ContainerFrame, OptionFrame
from ..core.window import Window

from .attacks import AttackFrame

from tkinter import Frame, Label, BOTH, TOP

##

class MainFrame(OptionFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_option("Social-Engineering Attacks", self.sub_to_attacks)
        self.add_option("Penetration Testing (Fast-Track)", self.sub_to_pentest)
        self.add_option("Third Party Modules", self.sub_to_thirdparty)
        self.add_option("Update the Social-Engineer Toolkit", self.sub_to_update)
        self.add_option("Update SET configuration", self.sub_to_config)
        self.add_option("Help, Credits, and About", self.sub_to_help)

        self.resize_window()

    def sub_to_attacks(self, *args, **kwargs):
        frame = self.master.get_frame("AttackFrame")
        frame.resize_window()
        frame.tkraise()

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

main_menu = Window("SE Toolkit", None)
main_menu.resizable(False, False)

container_frame = ContainerFrame(main_menu)
container_frame.pack(side=TOP, fill=BOTH, expand=True)

main_frame = container_frame.add_frame(MainFrame)
attack_frame = container_frame.add_frame(AttackFrame)

main_frame.tkraise()
