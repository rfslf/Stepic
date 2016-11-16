import numpy as np
IN = [int(i) for i in input().split()]
n = IN.pop(0)
m = IN.pop(0)
M = [[IN.pop(0) for j in range(m)] for i in range(n)]
MT = np.array(M).transpose()
for row in MT:
    for col in row:
        print(col, end = " ")
