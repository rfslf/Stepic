lst = input().split()
lst.sort()
i = 0
f = 0
while i < len(lst):
    f = lst.count(lst[i])
    if f == 1:
        i += 1
    else:
        print(lst[i], end=' ')
        i += f
