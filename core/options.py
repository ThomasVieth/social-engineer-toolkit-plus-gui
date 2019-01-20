##
##
##
##
##

## Imports

## All declaration for import *
__all__ = ('Section', 'Option', )

## Option Class
class Option(object):

    def __init__(self, text, on_select):
        self.text = text
        self.on_select = on_select

## Section Class
class Section(list):
    all_sections = list()

    def __init__(self, name):
        Section.all_sections.append(self)

        self.name = name

    def find_option_by_attr(self, attr, value):
        for option in self:
            if getattr(option, attr) == value:
                return option
        return None