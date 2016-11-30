s = str(input())
a = str(input())
b = str(input())
if a not in s:
    print(0)
elif a in b:
    print('Impossible')
else:
    n = 0
    while a in s:
        s = s.replace(a, b)
        n += 1
    print(n)
