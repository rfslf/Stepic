a, b = map(int, input().split())


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def lcm(x, y):
    l = (x * y)//gcd(x, y)
    return l
print(lcm(a, b))
