M = [[float(j) for j in input().split()] for i in range(4)]
R1 = (M[0][0] - M[1][0])**2 + (M[0][1] - M[1][1])**2
R2 = (M[0][0] - M[2][0])**2 + (M[0][1] - M[2][1])**2
print(min(R1, R2))