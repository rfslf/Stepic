n, m = map(int, input().split())

matrix = [list(input()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '.':  # в этой клетке мины нет, поэтому считаем число мин вокруг
            matrix[i][j] = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and matrix[ai][aj] == '*':
                        matrix[i][j] += 1
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end='')
    print()
