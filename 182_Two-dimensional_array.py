n, m = map(int, input().split())
S = [[0 for i in range(m)] for j in range(n)]
num = 1

if m >= n:
    for i in range(m):
        for j in range(min(i+1, n)):
            S[j][i-j] = num
            num += 1
    for i in range(n - 1):
        for j in range(n-i-1):
            S[i + j + 1][m - 1 - j] = num
            num += 1
