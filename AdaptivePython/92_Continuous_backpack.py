n, W = input().split(' ')
W = int(W)
a = list()

Max, C = 0, 0
for i in range(int(n)):
    a.append([int(i) for i in input().split(' ')])
for j in a:
    j.insert(0, j[0]/j[1])
a.sort()

while W > 0 and len(a) > 0:
    cost = a.pop()
    if W <= cost[2]:
        C += W*cost[0]
        W = 0
    else:
        W -= cost[2]
        C += cost[1]
print('%.3f' % C)