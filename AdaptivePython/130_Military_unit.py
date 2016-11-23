from bisect import bisect

Sin_line = []


def f(x, y):
    global Sin_line
    if x == 1:
        a = bisect(Sin_line, y)
        Sin_line.insert(a, y)
        print(len(Sin_line) - a - 1, end=' ')
    else:
        Sin_line.pop(len(Sin_line) - 1 - y)
        pass
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    f(x, y)
