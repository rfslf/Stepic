n, m = [int(i) for i in input().split()]

matrix = [list(input()) for i in range(n)]
M = list()

for i in range(n):
    M.append(list())
    for j in range(m):
        M[i].append(0)
        life = 0

        for di in [0, 1, -1]:
            for dj in [0, 1, -1]:
                if di == 0 and dj == 0:
                    continue
                ai = (n + i + di) % n
                aj = (m + j + dj) % m
                if matrix[ai][aj] == 'X':
                    life += 1
        if matrix[i][j] == '.':  # в этой клетке жизни нет, поэтому ищем жизнь вокруг
            if life == 3:
                M[i][j] = 'X'
            else:
                M[i][j] = '.'
        else:
            if life in [2, 3]:
                M[i][j] = 'X'
            else:
                M[i][j] = '.'

        print(M[i][j], end='')
    print()