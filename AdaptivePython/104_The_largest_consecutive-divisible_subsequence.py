n = int(input())
S = [int(i) for i in input().split()]
SS = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if S[i] % S[j] == 0 and SS[i] <= SS[j]:
            SS[i] = SS[j] + 1
print(max(SS))