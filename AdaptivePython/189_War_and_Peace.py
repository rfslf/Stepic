l = input().lower().split(' ')
d = {}
for i in l:
    d[i] = l.count(i)
for key in d:
    print(key, d[key])
