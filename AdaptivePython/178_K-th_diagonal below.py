n = int(input())
S = [[int(i) for i in input().split()] for j in range(n)]
m = int(input())
A = []

if m < 0:
    i = -m
    for j in range(n-i):
        A.append(S[j][i+j])

if m >= 0:
    i = m
    for j in range(n-i):
        A.append(S[i+j][j])
for a in A:
    print(a, end=' ')

