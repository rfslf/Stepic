n = int(input())
N = [int(i) for i in input().split(' ')]
l = []
for j in range(n):
    l.append([N[j], j+1])
l.sort()
for i in l:
    print(i[1], end=' ')