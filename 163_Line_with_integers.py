x = input().split(' ')
s = 0
for i in x:
    if i == '':
        continue
    else:
        s += int(i)
print(s)
