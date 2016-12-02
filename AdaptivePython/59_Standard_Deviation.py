a = []
S, sdev = 0, 0
while True:
    n = int(input())
    if n != 0:
        a.append(n)
    else:
        break
l = len(a)
for i in range(l):
    S += a[i]
for j in range(l):
    sdev += (a[j]-S/l)**2
print((sdev/(l-1))**(1/2))