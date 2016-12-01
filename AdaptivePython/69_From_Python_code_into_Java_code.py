x = input().split('_')
for i in range(len(x)):
    print(x[i][0].upper()+x[i][1:].lower(), end='')