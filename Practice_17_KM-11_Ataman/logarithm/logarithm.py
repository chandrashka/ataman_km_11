from math import log as lll
from math import *
def log(a,b):
    if a > 0 and a != 1 and b > 0:
        return lll(b,a)
def ln(b):
    if b > 0:
        return lll(b, e)
    else:
        return False

def lg(b):
    if b > 0:    
        return lll(b,10)
    else:
        return False