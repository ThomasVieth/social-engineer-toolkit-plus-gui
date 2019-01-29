##
##
##
##
##

## Imports
from tkinter import Tk

## All declaration for import *
__all__ = ('Window', )

## Window class extended from tkinter

class Window(Tk):
    all_windows = list()

    def __init__(self, title, owner, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Window.all_windows.append(self)

        self._owner = owner
        self._children = list()

        if issubclass(type(owner), Window):
            self._owner._children.append(self)

        self.title(title)

    def destroy(self, *args, **kwargs):
        'Destroys the current window and any children opened by the current window.'
        Window.all_windows.remove(self)

        if self._owner:
            self._owner._children.remove(self)

        for child in self._children:
            child.destroy()

        super().destroy(*args, **kwargs)