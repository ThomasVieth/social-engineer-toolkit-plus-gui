##
##
##
##
##

## Imports
from .hangable_window import HangableWindow

from ...config import get_config_parser_for

from functools import wraps
from tkinter import Label

##

config = get_config_parser_for("core")

##

class OptionWindow(HangableWindow):

    spacer = config.getint("menu", "y-spacer")
    x = config.getint("menu", "x-offset")
    y = config.getint("menu", "y-offset")
    font_type = config.get("font", "font-type")
    font_color = config.get("font", "font-color")
    font_size = config.getint("font", "font-size")

    def __init__(self, title, owner, *args, **kwargs):
        super().__init__(owner, *args, **kwargs)

        self.title(title)
        self.options = list()

    def display_options(self):
        y_spacer = self.y
        for text, option in self.options:
            label = Label(self, text=text, fg=self.font_color, font=(self.font_type, self.font_size))
            label.place(x=self.x, y=y_spacer)
            label.bind("<Button-1>", option)
            y_spacer += self.spacer

        size = self.spacer * round(y_spacer / self.spacer) + self.x
        self.geometry("256x{}".format(size))

    def add_option(self, text, method):
        self.options.append((text, method))