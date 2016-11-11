def IsPointInArea(x, y):
    return (((x+1)**2 + (y-1)**2 <= 4) and (y >= -x) and (y >= 2*x + 2)) or (((x+1)**2 + (y-1)**2 >= 4) and (y <= -x) and (y <= 2*x + 2))

x = int(input())
y = int(input())
solution = IsPointInArea(x, y)
if solution:
    print("YES")
else:
    print("NO")
