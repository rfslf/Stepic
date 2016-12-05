p = int(input())
x = int(input())
y = int(input())
k = int(input())
Dr, Cr = 0, 0
for i in range(k):
    X = x+x*p/100
    Y = y+y*p/100
    D = (X//1)+Y//100
    C = int(((X*100) % 100) + Y % 100)
    D = int(D+C//100)
    C %= 100
    x = D
    y = C
print(x, y)