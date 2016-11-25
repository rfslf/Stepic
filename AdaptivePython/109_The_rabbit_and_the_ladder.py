k, n = map(int, input().split())
R = [0 for i in range(n+1)]

for i in range(n+1):
    if i == 0:
        R[i] = 1
    else:
        jumps = 0
        for j in range(1, k+1):
            jumps += R[i-j]
        R[i] = jumps
print(R[-1])
