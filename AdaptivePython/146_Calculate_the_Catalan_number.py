from math import factorial


def fact(n):
    return factorial(n)


def cat_direct(n):
    return fact(2 * n) // fact(n + 1) // fact(n)


print(cat_direct(int(input())) % 1000000007)
