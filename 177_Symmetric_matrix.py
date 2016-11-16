import numpy as np

n = int(input())
S = [[int(i) for i in input().split()] for j in range(n)]
A = np.array(S)
if np.array_equal(A, A.transpose()):
    print('YES')
else:
    print('NO')
