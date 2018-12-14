##
##
##
##
##

## Imports
from .window import Window

from ..helpers import classproperty

## All declaration for import *
__all__ = ('HangableWindow', )

## HangableWindow class extended from window.<Window>

class HangableWindow(Window):

    def __init__(self, *args **kwargs):
        super().__init__(*args, **kwargs)

        self.is_hanging = False

    @classmethod
    def hangable_method(cls, method):
        def decorator(self, *args, **kwargs):
            if not self.is_hanging:
                return method(self, *args, **kwargs)
        return decorator

    @classproperty
    def hangable_windows(cls):
        return [window for window in cls.all_windows if hasattr(window, 'is_hanging')]

    @classproperty
    def hanging_windows(cls):
        return [window for window in cls.all_windows if hasattr(window, 'is_hanging') and window.is_hanging is True]

    @classproperty
    def non_hanging_windows(cls):
        return [window for window in cls.all_windows if hasattr(window, 'is_hanging') and window.is_hanging is False]