a = float(input())
b = float(input())
c = float(input())
D = (b**2) - 4*a*c
if D > 0:
    x1 = ((-b-D**(1/2))/(2*a))
    x2 = ((-b+D**(1/2))/(2*a))
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
elif D == 0:
    print((-b/(2*a)))