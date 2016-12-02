n = int(input())
a, i = 1, 1
while a <= n:
    for j in range(i):
        if a == n+1:
            break
        print(i, end=' ')
        a += 1
    i += 1