##
##
##
##
##

## Imports

## Class property decorator

class classproperty(object):
    'A new descriptor for stand-alone properties inside classes.'
    
    def __init__(self, fget=None, doc=None):
        'Initiates the getter and doc-string for the property.'
        self.fget = fget
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, cls=None):
        if cls is None:
            return self.fget(type(obj))
        return self.fget(cls)