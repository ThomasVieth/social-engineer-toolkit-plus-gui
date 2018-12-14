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

    def __init__(self, owner, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._owner = owner

    def __new__(cls, *args, **kwargs):
        instance = cls(*args, **kwargs)
        all_windows.append(instance)
        return instance