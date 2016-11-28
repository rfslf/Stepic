len_m, len_h = [int(i) for i in input().split()]
d = {}
for j in range(len_m):
    y1, y2 = [str(i) for i in input().split(': ')]
    d[y2] = y1

h = input()
H = ''
q = 0
while q < len_h:
    r = q + 1
    while r <= len_h:
        if h[q:r] in d:
            H += d[h[q:r]]
            q = r
            break
        else:
            r += 1
print(H)