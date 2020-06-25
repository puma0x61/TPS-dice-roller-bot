from random import choice
from .constants import EDGELORD_PARTS


def edgelord_feature():
    edginess = [choice(EDGELORD_PARTS[0]), choice(EDGELORD_PARTS[1]), choice(EDGELORD_PARTS[2]),
                choice(EDGELORD_PARTS[3])]
    return ' '.join(edginess)
