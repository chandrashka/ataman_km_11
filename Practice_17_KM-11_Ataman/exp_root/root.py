def root2(n):
    if type(n) == int or type(n) == float or type(n) == complex:
        if n > 0:
            return n ** 0.5
    else:
        return False
def root3(n):
    if type(n) == int or type(n) == float or type(n) == complex:
        return n ** (1/3)
    else:
        return False