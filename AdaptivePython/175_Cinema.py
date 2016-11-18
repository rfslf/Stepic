import re
n, m = map(int, input().split())
C = []
for i in range(n):
    C.append(input())
k = int(input())
sample = "0" + " 0" * (k - 1)
for row in range(n):
    search = re.search(sample, C[row])
    if search:
        print(row+1)
        break
else:
    print(0)
