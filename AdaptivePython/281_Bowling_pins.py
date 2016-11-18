N, K = [int(i) for i in input().split()]
pins = ['I'] * N
k = 0
while k < K:
    mi, ma = [int(i) for i in input().split()]
    for i in range(mi-1, ma):
        pins[i] = '.'
    k += 1
for j in pins:
    print(j, end='')
