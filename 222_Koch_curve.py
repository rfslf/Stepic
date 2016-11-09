def koch(order):
    if not order:
        return
    else:
        koch(order-1)   # Go 1/3 of the way
        print('turn', 60)
        koch(order-1)
        print('turn', -120)
        koch(order-1)
        print('turn', 60)
        koch(order-1)
koch(int(input()))
