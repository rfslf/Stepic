N = int(input())
l, r = map(int, input().split())
A = list(range(l, r))
for n in range(N-1):
    C = []
    l, r = map(int, input().split())
#    B = list(range(l, r))
#    while A and B:
    i = 0
    while l < r and :
        if A[i] > l:
#        if A[0] < B[0]:
            A.insert(i, l)
            i += 1
            l += 1
        else:
            i += 1
    if A:
        C.extend(A)
    else:
        C.extend(list(range(l, r)))
    A = C

def intervals(A):
    count = 0
    inter = True
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            if inter:
                count += 1
            else:
                inter = True
        else:
            inter = False
#        print(inter, count)
    if inter:
        count += 1
    return count
#print(A)
print(intervals(A))