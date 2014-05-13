from functools import wraps

__author__ = 'ippei_konishi'


def takes(*typy_args):
    def deco(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            assert all([TypyCondition(arg).meets() for arg in args])
            return f(*args, **kwargs)
        return wrapper
    return deco

class TypyCondition(object):
    def __init__(self, cond):
        pass

    def meets(self):
        return False