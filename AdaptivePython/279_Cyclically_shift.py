n = int(input())
arr = [int(i) for i in input().split()]
x = arr.pop()
arr.insert(0, x)
for j in arr:
    print(j, end=' ')
