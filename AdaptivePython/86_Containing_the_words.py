x = input().split(' ')
x.sort(key=len)
y = []
for i in x:
    y.append(len(i))
z = set(y)
for j in z:
    print(j, y.count(j), sep=': ')