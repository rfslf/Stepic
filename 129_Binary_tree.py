from heapq import heapify

N = int(input())
A = list(map(int, input().split()))


def heapify():
    global A
    '''Turns a list `A` into a max-ordered binary heap.'''
    n = len(A) - 1
    # start at last parent and go left one node at a time
    for node in range(n//2, -1, -1):
        __siftdown(node)
    return

def __siftdown(node):
    global A
    '''Traverse down a binary tree `A` starting at node `node` and
    turn it into a max-heap'''
    child = 2*node + 1
    # base case, stop recursing when we hit the end of the heap
    if child > len(A) - 1:
        return
    # check that second child exists; if so find max
    if (child + 1 <= len(A) - 1) and (A[child+1] > A[child]):
        child += 1
    # preserves heap structure
    if A[node] < A[child]:
        __swap(node, child)
        __siftdown(child)
    else:
        return

def __swap(i, j):
    global A
    # the pythonic swap
    A[i], A[j] = A[j], A[i]
    return


bh = heapify()

print(A)