a, b, c, d = int(input()), int(input()), int(input()), int(input())


def min(a, b):
    if a <= b:
        return a
    else:
        return b


def min4(a, b, c, d):
    z = min(a, b)
    y = min(c, d)
    return min(z, y)

print(min4(a, b, c, d))
