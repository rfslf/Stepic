x, y = [int(i) for i in input().split('/')]
lout = list()

while y != 0:
    a = x//y
    b = y
    y = x-a*y
    lout.append(a)
    x = b
for i in lout:
    print(i, end=' ')
