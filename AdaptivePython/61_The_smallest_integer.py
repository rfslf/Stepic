M = int(input())
n, N = 1, 1
while N <= M:
    n += 1
    N *= n
print(n)