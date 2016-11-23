n = int(input())
C = [int(i) for i in input().split(' ')]
C.sort()
for i in C:
    print(i, end=" ")
