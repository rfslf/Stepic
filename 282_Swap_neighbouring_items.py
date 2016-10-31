N = int(input())
arr = [int(i) for i in input().split()]
if N % 2 != 0:
    N -= 1
i = 0
while i < N:
    x = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = x
    i += 2
for j in arr:
    print(j, end=' ')
