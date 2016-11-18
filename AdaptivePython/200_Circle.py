def IsPointInCircle(x, y, xc, yc, r):
    X = (xc-x)
    Y = (yc-y)
    R = (X**2+Y**2)**(1/2)
    if R <= r:
        return True
    else:
        return False

x, y, xc, yc, r = float(input()), float(input()), float(input()), float(input()), float(input())
y = IsPointInCircle(x, y, xc, yc, r)
if y:
    print("YES")
else:
    print("NO")
