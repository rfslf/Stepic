matrix = list()
M = list()
a, b = [int(i) for i in input().split(' ')]  # a - row, b - column
for i in range(a):
    matrix.append([c for c in input().split(' ')])

for j in range(b):
    for q in range(a):
        print(matrix[q][j], end=' ')
    print()
