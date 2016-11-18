N = int(input())
R = []
for i in range(N):
    x, y = [int(i) for i in input().split()]
    ranger = (x**2 + y**2)
    R.append([ranger, [x, y]])
R.sort()
for i in R:
    print(i[1][0], i[1][1])
