lst = [int(i) for i in input().split()]
s, i = 0, 0
while i < len(lst):
    if lst[i] % 2 == 0:
        s += lst[i]
    if (i + 1) % 2 == 0:
        print(lst[i])
        i += 1
    else:
        i += 1
print(s)
