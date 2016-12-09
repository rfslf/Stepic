a = input().split()
x1 = int(a[0])
x2 = int(a[1])
y1 = int(a[2])
y2 = int(a[3])
f = 0
if x1 == y1 or x2 == y2:
    print('YES')
    f = 1
else:
    for i in range(8):
        if x1+i == y1 and x2+i == y2:
            print('YES')
            f = 1
            break
        elif x1-i == y1 and x2+i == y2:
            print('YES')
            f = 1
            break
        elif x1-i == y1 and x2-i == y2:
            print('YES')
            f = 1
            break
        elif x1+i == y1 and x2-i == y2:
            print('YES')
            f = 1
            break
if f == 0:
    print('NO')