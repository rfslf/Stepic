x = int(input())
y = list()
for x in range(x):
    z = input().split(' ')
    if z[0] == 'Insert':
        y.append(int(z[1]))
        flagsort = 0
    else:
        if flagsort == 0:
            y.sort()
            flagsort = 1
        print(y.pop())
