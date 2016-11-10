a = float(input())
b = int(input())


def power(x, y):
    if y != 1 and y != 0:
        if y % 2 == 0:
            return power(x*x, y/2)
        else:
            return x*power(x, y-1)
    elif y == 0:
        return 1
    else:
        return x
print(power(a, b))
