matrix = []
M = 0
a = 0 #row
b = 0 #column
while True:
    string = [c for c in input().split()]
    if string[0] == 'end':
        break
    else:
        matrix.append(string)
        a = len(string)
        b += 1
for i in range(b):
    for j in range(a):
        M = (int(matrix[i-1][j]))+(int(matrix[i-b+1][j]))+(int(matrix[i][j-1]))+(int(matrix[i][j-a+1]))
        print(M, end=' ')
    print()
