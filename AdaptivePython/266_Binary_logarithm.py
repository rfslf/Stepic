def f(v):
    for i in range(31):
        if 2**i > v:
            return i-1


n = int(input())
for i in range(n):
    x = int(input())
    print(f(x))
