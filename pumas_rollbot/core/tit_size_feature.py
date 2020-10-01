from random import choice
from .constants import TIT_SIZE 

def tit_size_feature():
    tittiness = [choice(TIT_SIZE[0]), choice(TIT_SIZE[1])]  
    return ' '.join(tittiness)
