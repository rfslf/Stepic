x = input().split(' ')
for i in range(len(x)-1):
    if x[i] != '':
        print(x[i], end="_")
if x[-1] != '':
    print(x[-1])