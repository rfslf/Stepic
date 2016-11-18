a = float(input())
b = float(input())


def IsPointInSquare(x, y):
    if abs(x+y) <= 1 and abs(x-y) <= 1:
        return True
    else:
        return False

z = IsPointInSquare(a, b)
if z:
    print("YES")
else:
    print("NO")
