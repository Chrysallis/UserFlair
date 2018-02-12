__author__ = 'night'

### a collection of helper functions designed for reddit bots

def clean(arg):
    """
    :param arg: string
    :return: removes leading or trailing whitespace and converts string to lowercase.
    """
    return str.lower(str.strip(arg))

