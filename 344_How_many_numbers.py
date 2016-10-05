n = int(input())
Numbs = [int(i) for i in input().split()]
Numbs.sort()
K = int(input())
for i in range(K):
    l, r = map(int, input().split())
    j = 0
    for num in Numbs:
        if l <= num <= r:
            j += 1
        elif num > r:
            break
    print(j, end=' ')
