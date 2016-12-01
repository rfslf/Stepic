x = input().split()
l, m = 0, -1
for i in range(len(x)):
    if len(x[i]) > l:
        l = len(x[i])
        m = i
print(x[m])