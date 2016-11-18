n = []
y = []
x = input().split(' ')
for i in range(len(x)-1):
    n.append(abs(int(x[i+1])-int(x[i])))
    y.append(i+1)
n.sort()

if len(x) == 1:
    print("Jolly")
elif n == y:
    print("Jolly")
else:
    print("Not jolly")
