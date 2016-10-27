import numpy as np
N = int(input())
M = np.array([[int(i) for i in input().split()] for j in range(N)])
if np.array_equal(M, M.T):
    print('YES')
else:
    print('NO')
