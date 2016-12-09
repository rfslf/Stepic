n = int(input())
m = int(input())
k = int(input())
flag = 0
for i in range(m+1):
    if i*n == k:
        print("YES")
        flag = 1
for j in range(n+1):
    if j*m == k:
        if flag != 1:
            print("YES")
            flag = 1
if flag != 1:
    print("NO")