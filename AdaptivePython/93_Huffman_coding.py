n = list(input())
m = set(n)
x = list()
d = {}

for i in m:
    x.append([n.count(i),i])

x.sort(reverse=True)
q = x.copy()
D = {}

if len(x) > 1:
    while len(x) > 1:
        y1 = x.pop()
        y2 = x.pop()
        y = [int(y1[0])+int(y2[0]), y2[1]+y1[1]]
        x.append(y)
        x.sort(reverse=True)
        D[y2[1]+y1[1]] = [y2[1], y1[1]]
        start = (y2[1]+y1[1])

    for j in m:
        d[j] = ''
        z = j
        while z != start:
            for i in D:
                if D[i][0] == z:
                    z = i
                    d[j] += '0'
                elif D[i][1] == z:
                    z = i
                    d[j] += '1'
else:
    d[n[0]] = '0'
for k in d:
    d[k] = d[k][::-1]

H = list()
for j in n:
    H.append(d[j])
h = "".join([str(i) for i in H])
print(len(m), len(h))
for k in q:
    print(k[1], ": ", d[k[1]], sep='')
print(h)
