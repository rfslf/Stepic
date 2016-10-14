from heapq import heapify

N = int(input())
A = list(map(int, input().split()))

def heapify():
    global A
    for i in range(len(A) // 2, -1, -1):
        siftDown(i)


#def insert(key):
#    global A
#    A.heapSize = a.heapSize + 1
#    a[a.heapSize - 1] = key
#    siftUp(a.heapSize - 1)

def siftDown(i):
    global A
    while 2 * i + 2 < len(A):     # heapSize — количество элементов в куче
        left = 2 * i + 1             # left — левый сын
        right = 2 * i + 2            # right — правый сын
        j = left
        if right < len(A) and A[right] < A[left]:
            j = right
        if A[i] <= A[j]:
            if A[right] > A[left]:
                A[right], A[left] = A[left], A[right]
            break
        A[i], A[j] = A[j], A[i]
        if A[right] > A[left]:
            A[right], A[left] = A[left], A[right]
        i = j


bh = heapify()
for i in A:
    print(i, end=' ')
