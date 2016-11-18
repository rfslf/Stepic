a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
else:
    b = [0]*len(a)
    for j in range(len(a)):
        b[j] = int(a[j-1]+a[j-len(a)+1])
        print(b[j], ' ', end='')
