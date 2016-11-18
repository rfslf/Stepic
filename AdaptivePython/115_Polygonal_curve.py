N = int(input())
Co = []
for i in range(N):
    a, b = map(int, input().split())
    Co.append([a, b])
Co.sort()
for c in Co:
    print(c[0], c[1])
print(Co)
i = 0
while i < N:
    for j in range(i,N):
        if Co[i][0] == Co[j][0]:
            if Co[i][1] > Co[j][1]:
                Co[i], Co[j] = Co[j], Co[i]
        else:
            break
    i += 1
print(Co)