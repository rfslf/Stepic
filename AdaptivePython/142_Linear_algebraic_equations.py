import numpy
n, m = map(int, input().split())
N = []
M = []
for i in range(n):
    In = [int(i) for i in input().split()]
    M.append(In.pop())
    N.append(In)

if n < m:
    print("INF")
else:
    try:
        x = numpy.linalg.solve(numpy.array(N), numpy.array(M))
    except numpy.linalg.linalg.LinAlgError:
        print('NO')
    else:
        print("YES")
        for i in x:
            print(i, end=' ')
