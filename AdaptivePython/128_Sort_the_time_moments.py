x = []
n = int(input())

for i in range(n):
    z = []
    a, b, c = input().split(' ')
    z = [int(a)*3600 + int(b)*60 + int(c), a, b, c]
    x.append(z)
x.sort()
for j in range(len(x)):
    print(int(x[j][1]), int(x[j][2]), int(x[j][3]))