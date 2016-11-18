D = {}
n = int(input())
for i in range(n):
    y = int(input())
    if y not in D:
        z = f(y)
        print(z)
        D[y] = z
    else:
        print(D[y])
