N = int(input())
M = [['*'] * (N+2) for i in range(N+2)]
for i in range(1, N+1):
    for j in range(1, N+1):
        M[i][j] = 0
k = 1
d = 'r'
x = 1
y = 0
while k <= N**2:
    while d == 'r':
        if M[x][y+1] == 0:
            y += 1
            M[x][y] = k
            k += 1
        else:
            d = 'd'
    while d == 'd':
        if M[x+1][y] == 0:
            x += 1
            M[x][y] = k
            k += 1
        else:
            d = 'l'
    while d == 'l':
        if M[x][y-1] == 0:
            y -= 1
            M[x][y]=k
            k += 1
        else:
            d = 'u'
    while d == 'u':
        if M[x-1][y] == 0:
            x -= 1
            M[x][y] = k
            k += 1
        else:
            d = 'r'
for i in range(1, N+1):
    for j in range(1, N+1):
        print(M[i][j], end=' ')
    print()
