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
        instance = super().__new__(cls)
        cls.all_windows.append(instance)
        return instance

    def destroy(self, *args, **kwargs):
        Window.all_windows.remove(self)

        super().destroy(*args, **kwargs)