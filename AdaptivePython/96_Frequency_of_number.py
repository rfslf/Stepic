n = int(input())//2
lst = [int(i) for i in input().split()]
Di = {}
for j in lst:
    if not Di.get(j):
        Di[j] = 1
    else:
        Di[j] += 1
flag = 0
for k in Di:
    if Di[k] > n:
        flag = 1
        print(1)
        break
if flag == 0:
    print(0)