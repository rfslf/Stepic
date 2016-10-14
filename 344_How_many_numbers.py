n = int(input())
Numbs = list(map(int, input().split()))


for i in Numbs:
    for j in range(i, M):
#        print(i,j)
        book[j] += 1
K = int(input())
for i in range(K):
    l, r = map(int, input().split())
    if l > M:
        print(0, end=' ')
    else:
        if r > M:
            r = M
        print(book[r-1] - book[l-1], end=' ')
#print(book)
#    j = 0
#    for num in Numbs:
#        if l <= num <= r:
#            j += 1
#        elif num > r:
#            break
#    print(j, end=' ')
