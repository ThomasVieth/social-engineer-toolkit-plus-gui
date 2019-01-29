##
##
##
##
##

## Imports
from ..config import get_config_parser_for

from functools import wraps
from tkinter import Frame, Label, BOTH, TOP, W

## All declaration for import *
__all__ = ('ContainerFrame', 'HangableFrame', 'OptionFrame', )

##

config = get_config_parser_for("core")

## 

class ContainerFrame(Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frames = {}

    def add_frame(self, cls):
        frame = cls(master=self)
        self.frames[cls.__name__] = frame

        frame.grid(row=0, column=0, sticky="nsew")
        return frame

    def get_frame(self, name):
        return self.frames.get(name, None)

## HangableWindow class extended from tkinter.<Frame>

class HangableFrame(Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_hanging = False

    def destroy(self, *args, **kwargs):
        super().destroy(*args, **kwargs)

        self.is_hanging = False

    @classmethod
    def hangable_method(cls, method):
        @wraps(method)
        def decorator(self, *args, **kwargs):
            if not self.is_hanging:
                return method(self, *args, **kwargs)
        return decorator

##

class OptionFrame(HangableFrame):

    width = config.getint("window", "width")
    spacer = config.getint("menu", "y-spacer")
    x = config.getint("menu", "x-offset")
    y = config.getint("menu", "y-offset")
    font_type = config.get("font", "font-type")
    font_color = config.get("font", "font-color")
    font_size = config.getint("font", "font-size")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.labels = list()

    @property
    def vertical_size(self):
        return OptionFrame.y + (OptionFrame.spacer * len(self.labels))

    def resize_window(self):
        size = self.vertical_size + OptionFrame.x
        self.master.master.geometry("{}x{}".format(OptionFrame.width, size))

    def add_option(self, text, method):
        label = Label(self, text=text, fg=OptionFrame.font_color,
            font=(OptionFrame.font_type, OptionFrame.font_size))
        label.bind("<Button-1>", method)
        label.pack(side=TOP, anchor=W, padx=(OptionFrame.x, 0), pady=(OptionFrame.spacer/2, 0))
        self.labels.append(label)