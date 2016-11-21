# put your python code here
import numpy
n, m = map(int, input().split())
A, C = list(), []
for i in range(n):
    a = input().split()
    A.append(a[:-1])
    C.append(a[-1])
x = numpy.linalg.lstsq(A, C)[0]
for i in range(m):
    print(x[i], end=' ')
