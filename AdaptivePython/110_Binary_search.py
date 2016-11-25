n = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]
m.pop(0)


def binSearch(x):
    global n
    l = 0
    r = len(n)
    while r - l > 1:
        m = (l + r) // 2
        if x < n[m]:
            r = m
        else:
            l = m
    return l if n[l] == x else -1

z = [print(i, end=' ') for i in map(binSearch, m)]