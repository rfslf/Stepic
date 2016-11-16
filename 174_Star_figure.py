n = int(input())
X = [['.' for j in range(n)] for i in range(n)]
h = n // 2

for i in range(n):
    X[i][-1 - i] = "*"
    X[i][i] = "*"

for row in X:
    row[h] = "*"
X[h] = ["*"] * n

for row in X:
    for col in row:
        print(col, end=" ")
    print()
