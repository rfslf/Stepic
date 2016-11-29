login = 100500
password = 424242
x = input().split(' ')
z = x[1]
y = x[0]
if int(y) == login and int(z) == password:
    print('Login success')
elif int(y) == login and int(z) != password:
    print('Wrong password')
else:
    print('No user with login', x[0], 'found')