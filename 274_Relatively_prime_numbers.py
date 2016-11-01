N = int(input())


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            while (n % d) == 0:
                n //= d
            primfac.append(d)
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


def Euler(n):
    counter = n
    Z = primes(n)
    for i in Z:
        counter *= (i - 1)
        counter //= i
    return counter
print(Euler(N))
