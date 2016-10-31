N = int(input())
N = 2*N - 1
#M = list()
M = [[1] * N for i in range(N)]

for a in range(1, N-1):
    for b in range(a,N-a):
        for c in range(a, N-a):
            M[b][c] += 1
for i in range(N):
    for j in range(N):
            print(M[i][j], end=' ')
    print()
