from random import choice

from .constants import TIT_REQUEST_SERVICE

def tit_request():
    return choice(TIT_REQUEST_SERVICE)

