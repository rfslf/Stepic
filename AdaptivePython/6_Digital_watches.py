T = int(input())
h = T//3600 % 24
m = T % 3600//60
s = T % 3600 % 60
print(h, end=':')
if m < 10:
    print('0', m, end=':', sep='')
else:
    print(m, end=':')
if s < 10:
    print('0', s, sep='')
else:
    print(s)