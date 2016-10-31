n, shift = input().split()
arr = [int(i) for i in input().split()]
i = 0
while i < int(shift):
    x = arr.pop(0)
    arr.append(x)
    i += 1
for j in arr:
    print(j, end=' ')
