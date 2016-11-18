from operator import itemgetter
n = int(input())
D = list()
for i in range(n):
    x, y = map(int, input().split())
    D.append([y, -x])
OL = sorted(D, key=itemgetter(0, 1), reverse=True)
for i in OL:
    print(-i[1], i[0])
