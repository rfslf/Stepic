n, m = map(int, input().split())
M = []
x, y, z = 1, m + 1, 1
for i in range(n):
    A = [j for j in range(x, y)]
    if z < 0:
        A.reverse()
    x, y, z = y, y+m, -z
    M.append(A)
for row in M:
    for col in row:
        print("{:4d}".format(col), end="")
    print()
