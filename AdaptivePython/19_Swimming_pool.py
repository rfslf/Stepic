n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n >= m:
    N = n
    M = m
else:
    N = m
    M = n
if 2 * x > M:
    X = M - x
else:
    X = x
if 2*y > N:
    Y = N-y
else:
    Y = y
if X >= Y:
    print(Y)
else:
    print(X)