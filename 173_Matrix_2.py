N = int(input())
M = [[0] * N for _ in range(N)]
i, j = 0, 0
k = 0
for i in range(N):
    for j in range(N):
        if i < j:
            M[i][j] = (j-i) % N
        if i > j:
            M[i][j] = (i-j) % N
for i in range(N):
    for j in range(N):
        print(M[i][j], end=' ')
    print()
