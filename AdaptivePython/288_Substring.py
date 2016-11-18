s = str(input())
t = str(input())
i = 0
j = 0
while i < len(s):
    x = s.find(t, i)
    i = 0
    if x != -1:
        i += x + 1
        j += 1
    else:
        break
print(j)
