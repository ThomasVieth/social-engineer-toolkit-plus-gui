##
##
##
##
##

## Imports
from configparser import ConfigParser
from os import getcwd, pardir
from os.path import abspath, isfile, join

## Getting configuration directory

current_working_directory = getcwd()

## Configuration cache

cache = dict()

## Parsing of the configuration file

def get_config_parser_for(name):
    'Returns a configparser.ConfigParser object with the configuration file specified parsed in.'
    if name in cache:
        return cache[name]

    file = join(current_working_directory, name + '.ini')
    if not isfile(file):
        raise ValueError('Configuration file for ' + name + ' is non-existent.')

    parser = ConfigParser()
    parser.read(file)
    cache[name] = parser
    return parser