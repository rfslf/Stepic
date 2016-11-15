n, m = map(int, input().split())
M = []
flag = True
seq = 1
for i in range(n):
    if i % 2 == 0:
        flag = True
    else:
        flag = False
    M.append([])
    for j in range(m):
        if flag:
            M[i].extend([seq])
            seq += 1
            flag = False
        else:
            M[i].extend([0])
            flag = True
    for col in M[i]:
        print("{:>4}".format(col), end="")
    print()
