def sum(a, b):
    if not(isinstance(a, int) and isinstance(b, int)):
        raise TypeError
    elif a <= 0 or b <= 0:
        raise ValueError
    else:
        return a+b
