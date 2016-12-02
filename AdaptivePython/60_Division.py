x = int(input())


def dev3(a):
    num = str(a)
    l = len(num)
    s, y = 0, 0
    for i in range(l):
        s += int(num[i])
    if s > 9:
        s = dev3(s)
    return(s)
if dev3(x) == 3 or dev3(x) == 6 or dev3(x) == 9:
    print('YES')
else:
    print('NO')