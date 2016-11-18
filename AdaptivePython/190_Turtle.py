n = 'North'
w = 'West'
s = 'South'
e = 'East'
d = {n: 0, w: 0, s: 0, e: 0}
t = int(input())
for i in range(t):
    napr = input().split()
    d[napr[0]] += int(napr[1])
print(d[e]-d[w], d[n]-d[s])
