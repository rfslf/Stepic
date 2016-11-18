lst = [int(i) for i in input().split()]
x = int(input())
j = 0
z = lst.count(x)
if z == 0:
    print('Missing')
else:
    for i in range(z):
        y = lst.index(x, j)
        print(y, end=' ')
        j = 1+y
