a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = 0
for x in range(1000):
    if a*(x**3)+b*x**2+c*x+d == 0:
        print(x)