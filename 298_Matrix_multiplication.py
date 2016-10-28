import numpy as np
n = int(input())
A = np.array([[int(k) for k in input().split()] for j in range(n)])
B = np.array([[int(k) for k in input().split()] for j in range(n)])

C = np.dot(A, B)

for row in C:
    for element in row:
        print(element, end=" ")
    print('')
