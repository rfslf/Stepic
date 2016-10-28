x1, x2, y1, y2 = map(int, input().split())
x1 -= 1
x2 -= 1
y1 -= 1
y2 -= 1
bol = True
for i in range(1,8):
    if (x1 + i) % 8 == y1 and (x2 + i) % 8 == y2:
        bol = True
        break
    elif (x1 - i)% 8 == y1 and (x2 + i) % 8 == y2:
        bol = True
        break
    else:
        bol = False

if x1 == y1 or x2 == y2 or bol:
    print('YES')
else:
    print("NO")