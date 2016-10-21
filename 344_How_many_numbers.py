import bisect
n = int(input())
Numbs = list(map(int, input().split()))
Numbs.sort()

K = int(input())
for i in range(K):
    l, r = map(int, input().split())
#    print(l, r)
    counter_L = bisect.bisect_left(Numbs, l)
    counter_R = bisect.bisect(Numbs, r)
    print(counter_R - counter_L, end=' ')
#print(book)
#    j = 0
#    for num in Numbs:
#        if l <= num <= r:
#            j += 1
#        elif num > r:
#            break
#    print(j, end=' ')
