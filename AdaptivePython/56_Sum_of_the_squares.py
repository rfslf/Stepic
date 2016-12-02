summa, square = 0, 0
while True:
    x = int(input())
    summa += x
    square += x**2
    if summa == 0:
        print(square)
        break