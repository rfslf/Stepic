n = [int(i) for i in input().split(' ')]
d, p = [], []
for i in range(len(n)):
    d.append(1)
    p.append(-1)

for i in range(len(n)):
    for j in range(i):
        if n[j] < n[i] and d[j] > d[i] - 1:
            d[i] = d[j] + 1
            p[i] = j

pos = d.index(max(d))
k = p[pos]
ans = []

while k != -1:
    ans.append(n[pos])
    pos = k
    k = p[pos]
ans.append(n[pos])
ans.reverse()

for i in ans:
    print(i, end=' ')
