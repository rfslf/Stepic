a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a != 0 and b != 0:
    if c != 0 and d != 0:
        # параллельны или линейное решение
        if a*d == c*b:
            if e*d == f*b:
                print('1', -a/b, e/b)
            else:
                print('0')
        # 2 dots
        else:
            x = (d*e-b*f)/(a*d-b*c)
            y = (a*f-c*e)/(a*d-b*c)
            print('2', x, y)
    elif c != 0 and d == 0:
        # 1 dots, x-const
        print('2', f/c, (e-a*f/c)/b)
    elif c == 0 and d != 0:
        # 1 dots, y-const
        print('2', (e-b*f/d)/a, f/d)
    else:
        #вся 1 линия
        if f == 0:
            print('1', -a/b, e/b)
        else:
            print('0')
elif a != 0 and b == 0:
    if c != 0 and d == 0:
        # параллельны или линейное решение
        if a*f == c*e:
            print('3', e/a)
        else:
            print('0')
    elif c == 0 and d != 0:
        # 1 dots
        y = f/d
        x = e/a
        print('2', x, y)
    elif c != 0 and d != 0:
        # 1 dots, x-const
        print('2', e/a, (f-c*e/a)/d)
    else:
        # вся 1 линия
        if f == 0:
            print('3', e/a)
        else:
            print('0')
elif a == 0 and b != 0:
    if c == 0 and d != 0:
        # параллельны или линейное решение
        if b*f == e*d:
            print('4', e/b)
        else:
            print('0')
    elif c != 0 and d == 0:
        # 1 dots
        y = e/b
        x = f/c
        print('2', x, y)
    elif c != 0 and d != 0:
        # 1 dots, y-const
        print('2', (f-d*e/b)/c, e/b)
    else:
        # вся 1 линия
        if f == 0:
            print('4', e/b)
        else:
            print('0')
else:
    if e == 0:
        if c != 0 and d != 0:
            # линейное решение
            print('1', -c/d, f/d)
        elif c != 0 and d == 0:
            # 1 dots
            print('3', f/c)
        elif c == 0 and d != 0:
            # 1 dots, y-const
            print('4', f/d)
        else:
            if f == 0:
                print('5')
            else:
                print('0')
    else:
        print('0')