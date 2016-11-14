# так решать нельзя!
x = input().split()
X = set(x)
y = input().split()
Y = set(x)
z = list()
for i in x:
    if i not in y:
        z.append(i)
for j in y:
    if j not in x:
        z.append(j)
Z = set(z)
for k in Z:
    print(k, end=" ")
