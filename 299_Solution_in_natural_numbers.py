N = int(input())
n = int(N ** 0.5) + 1
z = 0
for x in range(n):
    y = (N - x ** 2) ** 0.5
    if y % 1 == 0:
        print(x, int(y))
        z = 1
        break
if z == 0:
    print('No solution')
