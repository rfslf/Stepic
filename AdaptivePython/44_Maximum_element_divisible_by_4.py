n = int(input())
s = 0
for i in range(n):
    x = int(input())
    if x % 4 == 0 and x > s:
        s = x
print(s)