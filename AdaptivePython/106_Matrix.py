n, m = map(int, input().split())
M = [[int(i) for i in input().split()] for j in range(n)]
#print(M)

summa = M[0][0]

for i in range(n):
    for j in range(i, n):
        for k in range(m):
            for l in range(k, m):
#                print(i,j,k,l)
                if i == j and k == l:
                    s = M[i][k]
                elif i == j and k != l:
                    s = sum([M[i][x] for x in range(k, l+1)])
                elif i != j and k == l:
                    s = sum([M[x][k] for x in range(i, j+1)])
                else:
                    s = 0
                    for x in range(i,j+1):
                        s += sum([M[x][y] for y in range(k, l+1)])
                if s >= summa:
                    summa = s
print(summa)
