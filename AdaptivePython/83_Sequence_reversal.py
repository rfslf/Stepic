x = input().split()
y = int(x[0])
for i in range(int(x[0])//2):
    print(int(x[i+1])+int(x[-1-i]), end=' ')
if (y % 2) != 0:
    print(x[int((y+1)/2)])