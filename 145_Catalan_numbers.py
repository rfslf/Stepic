from math import factorial


def fact(n):
    return factorial(n)


def cat_direct(n):
    p = 1000000007
    return fact(2 * n) * pow((fact(n)*fact(n+1)), (p-2), p)


print(cat_direct(int(input())) % 1000000007)
