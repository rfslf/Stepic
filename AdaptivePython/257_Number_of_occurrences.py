s = str(input())
t = str(input())
n = 0
c = 0
while n < len(s):
    b = s.find(t, n)
    if b == -1:
        break
    n = b+1
    c += 1
print(c)
