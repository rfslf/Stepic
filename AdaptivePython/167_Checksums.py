n = int(input())
x = input().split(' ')
s = 0
for i in x:
    if i=='':
        continue
    else:
        s = (s + int(i))*113 % 10000007
print(s)
