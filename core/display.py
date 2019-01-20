##
##
##
##
##

## Imports
from .windows import Window, HangableWindow
from .options import Section, Option
from ..config import get_config_parser_for

from tkinter import Menu, Label, E, LEFT

##

config = get_config_parser_for("core")

##

def create_and_display_section(section, parent=None):
    window = Window(parent)

    spacer = config.getint("menu", "y-spacer")
    x = config.getint("menu", "x-offset")
    y = config.getint("menu", "y-offset")
    font_type = config.get("font", "font-type")
    font_color = config.get("font", "font-color")
    font_size = config.getint("font", "font-size")

    window.title(section.name)
    window.geometry("256x{}".format(
        spacer * len(section) + x
        )
    )
    window.items = list()

    for option in section:
        label = Label(window, text=option.text, fg=font_color, font=(font_type, font_size))
        label.place(x=x, y=y)
        label.bind("<Button-1>", option.on_select)
        window.items.append(label)
        y += spacer

    return window