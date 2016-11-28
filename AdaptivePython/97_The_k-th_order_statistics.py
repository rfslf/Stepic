n, k = map(int, input().split())
A = list(map(int, input().split()))

l_ptr = 0
r_ptr = n


def partition(l, r):
    global A
    x = A[l]
    j = l
    for i in range(l+1, r):
        if A[i] <= x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j

while True:
    p = partition(l_ptr, r_ptr)
    if p == k:
        print(A[p])
        break
    elif p < k:
        l_ptr = p + 1
    else:
        r_ptr = p
