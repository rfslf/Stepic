try:
    arr = [int(i) for i in input().split()]
    L = len(arr)
    if L % 2 != 0:
        L -= 1
    for i in range(L-1, 0, -2):
        print(arr[i], end=' ')
except Exception:
    print()
