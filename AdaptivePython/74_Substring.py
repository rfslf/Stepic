x = str(input())
y = str(input())
ind = 0
z = 1
while True:
    ind = x.find(y, ind)
    if ind == -1:
        if z == 1:
            print('-1')
        break
    print(ind, end=" ")
    z = 0
    ind += 1