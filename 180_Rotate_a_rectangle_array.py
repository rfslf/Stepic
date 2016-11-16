import numpy as np

n, m = map(int, input().split())
S = [[int(i) for i in input().split()] for j in range(n)]

A = np.array(S)
a = np.rot90(A, 3)
for row in a:
    for i in row:
        print(i, end=' ')
    print()
