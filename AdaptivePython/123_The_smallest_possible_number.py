x,y = input().split()
m = list(x)
m.reverse()
n = list(y)
n.reverse()
z = []
while True:
    a = m.pop()
    b = n.pop()
    if a < b:
        z.append(a)
        n.append(b)
    else:
        z.append(b)
        m.append(a)
    if len(n) == 0:
        m.reverse()
        z.extend(m)
        break
    if len(m) == 0:
        n.reverse()
        z.extend(n)
        break
for j in z:
    print(j, sep='', end='')