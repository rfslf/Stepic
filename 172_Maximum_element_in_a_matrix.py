n, m = input().split()
N = int(n)#Строки
M = int(m)#Столбцы
Ma = []
for i in range(N):
    y = [int(j) for j in input().split()]
    Ma.append(y)
s = Ma[0][0]
I = 0
J = 0
for q in range(N):
    for r in range(M):
        if Ma[q][r] > s:
            s = Ma[q][r]
            I = q
            J = r
print(I, J)
