S = input()
for i in S:
    if i == 'A':
        print('00', end='')
    elif i == 'C':
        print('01', end='')
    elif i == 'G':
        print('10', end='')
    else:
        print('11', end='')
