from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

indx = 0
for i in B:
#    indx = bisect_left(A, i, lo=indx)
    indx = bisect_left(A, i)
    if indx == 0:
        print(0, end=' ')
    elif indx >= N:
        print(N-1, end=' ')
    else:
        if abs(i - A[indx]) >= abs(i - A[indx-1]):
            print(indx-1, end=' ')
        else:
            print(indx, end=' ')
