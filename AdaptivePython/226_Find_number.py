def num(x):
    z = x
    S = 0
    count = 0
    for i in str(x):
       S += int(i)
    while z > 9:
        z -= 9
        q = str(z)
        s = 0
        for j in q:
            s += int(j)
        if s == S:
            count += 1
    return count
X = int(input())
print(num(X))
