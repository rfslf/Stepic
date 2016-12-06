A = int(input())
B = int(input())
S = 0
k = 0
for j in range(A, B+1):
    if j % 3 == 0:
        S += j
        k += 1
print(S/k)