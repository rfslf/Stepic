F = input()
if F == "triangle":
    a = float(input())
    b = float(input())
    c = float(input())
    P = (a+b+c)/2
    S = (P*(P-a)*(P-b)*(P-c)) ** 0.5
    print(S)
if F == 'rectangle':
    a = float(input())
    b = float(input())
    print(a*b)
if F == 'circle':
    a = float(input())
    print((a*a)*3.14)