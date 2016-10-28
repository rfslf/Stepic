x, y = map(float, input().split())
if (((x+3)**2 + (y+3)**2 <= 9) and (y >= (x+4)**2-4)) or ((y >= x) and ((x-3)**2 + (y+3)**2 <= 25)):
    print("YES")
else:
    print("NO")
