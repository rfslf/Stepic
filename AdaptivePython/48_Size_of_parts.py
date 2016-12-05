n = int(input())
rdy, fix, rej = 0, 0, 0
for j in range(n):
    i = int(input())
    if i == 0:
        rdy += 1
    elif i==1:
        fix += 1
    elif i == -1:
        rej += 1
print(rdy, fix, rej)