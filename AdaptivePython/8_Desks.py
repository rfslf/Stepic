a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0:
    A = a/2
else:
    A = (1+a)/2
if b % 2 == 0:
    B = b/2
else:
    B = (1+b)/2
if c % 2 == 0:
    C = c/2
else:
    C = (1+c)/2
print(int(A+B+C))