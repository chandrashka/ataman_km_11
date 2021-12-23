def fact(n):
    if type(n) != int or n <= 0:
        return False
    elif n == 1:
        return n
    else:
        return n * fact(n-1)
