a1 = ' -- '
a2 = '|  |'
a3 = '    '
a4 = '   |'
a5 = '|   '

d = {'0': [a1, a2, a2, a3, a2, a2, a1],
     '1': [a3, a4, a4, a3, a4, a4, a3],
     '2': [a1, a4, a4, a1, a5, a5, a1],
     '3': [a1, a4, a4, a1, a4, a4, a1],
     '4': [a3, a2, a2, a1, a4, a4, a3],
     '5': [a1, a5, a5, a1, a4, a4, a1],
     '6': [a1, a5, a5, a1, a2, a2, a1],
     '7': [a1, a4, a4, a3, a4, a4, a3],
     '8': [a1, a2, a2, a1, a2, a2, a1],
     '9': [a1, a2, a2, a1, a4, a4, a1]}

x = list(input())
l = len(x)
if l == 1:
    width = 4
else:
    width = (l - 1) * 5 + 4

print('x', '-' * width, 'x', sep='')

for i in range(7):
    print('|', end='')
    j = 1
    print(d[x[0]][i], end='')
    while j < len(x):
        print(' ' + d[x[j]][i], end='')
        j += 1
    print('|')

print('x', '-' * width, 'x', sep='')
