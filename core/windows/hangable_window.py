##
##
##
##
##

## Imports
from .window import Window

from ..helpers import classproperty

from functools import wraps

## All declaration for import *
__all__ = ('HangableWindow', )

## HangableWindow class extended from window.<Window>

class HangableWindow(Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_hanging = False

    @classmethod
    def hangable_method(cls, method):
        @wraps(method)
        def decorator(self, *args, **kwargs):
            if not method.is_hanging:
                return method(self, *args, **kwargs)
        return decorator

    @classproperty
    def hangable_windows(cls):
        'Returns a list of all running hangable windows.'
        return [window for window in cls.all_windows if hasattr(window, 'is_hanging')]

    @classproperty
    def hanging_windows(cls):
        'Returns a list of all currently hanging windows.'
        return [window for window in cls.all_windows if hasattr(window, 'is_hanging') and window.is_hanging is True]

    @classproperty
    def non_hanging_windows(cls):
        'Returns a list of all hangable windows that are not hanging.'
        return [window for window in cls.all_windows if hasattr(window, 'is_hanging') and window.is_hanging is False]