x = int(input())
y = list()
s, i = 0, 1
while s < x:
    s += i
    y.append(i)
    i += 1
z = s-x
if z:
    y.remove(z)
print(len(y))
for i in y:
    print(i, end=' ')
