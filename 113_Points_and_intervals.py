import bisect
n, m = map(int, input().split())
border = []



def check(i):
    global L, R
    counter_L = bisect.bisect(L, i)
    counter_R = bisect.bisect_left(R, i)
    return counter_L - counter_R


L, R = [], []
for i in range(n):
    l, r = map(int, input().split())
    bisect.insort(L, l)
    bisect.insort(R, r)

for i in input().split():
    print(check(int(i)), end=' ')


