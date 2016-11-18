x1, x2, y1, y2 = map(int, input().split())
X = [x1, x2]
Y = [y1, y2]
hops = [[x1 + 2, x2 - 1], [x1 + 2, x2 + 1], [x1 - 2, x2 + 1], [x1 - 2, x2 - 1], [x1 + 1, x2 + 2], [x1 + 1, x2 - 2],
        [x1 - 1, x2 + 2], [x1 - 1, x2 - 2]]
if Y in hops:
    print("YES")
else:
    print('NO')
