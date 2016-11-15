n, m = map(int, input().split())
M = [input().split() for _ in range(n)]
i, j = map(int, input().split())
for row in M:
    row[i], row[j] = row[j], row[i]
    for col in row:
        print(col, end=' ')
    print()
