a = float(input())
b = float(input())


def IsPointInSquare(x, y):
    if abs(x) <= 1 and abs(y) <= 1:
        return True
    else:
        return False
z = IsPointInSquare(a, b)
if z:
    print("YES")
else:
    print("NO")
