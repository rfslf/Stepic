n = int(input())
d = dict()
for i in range(n):
    w, s = input().split()
    d[s] = w
    d[w] = s
question = input()
print(d[question])
