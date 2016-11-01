N = int(input())
arr = [int(i) for i in input().split()]
i, count = 0, 0
while i < N-1:
    j = i + 1
    while j < N:
        if arr[i] == arr[j]:
            count += 1
        j += 1
    i += 1
print(count)
