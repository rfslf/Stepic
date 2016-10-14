n = int(input())
A = list(map(int, input().split()))
k = int(input())

i = 0
while i < n:
    for j in range(i, min(i+k, n)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

    print(A[i], end=" ")
    i += 1
