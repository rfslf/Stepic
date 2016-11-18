def collatz(n):
    if n != 1:
        print(int(n), end=" ")
        if not n % 2:
            m = n/2
            n = m
        else:
            m = 3*n+1
            n = m
        return collatz(n)
    else:
        print(1)
x = int(input())
collatz(x)
