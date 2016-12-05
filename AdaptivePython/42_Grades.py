n = int(input())
A, B, C, D = 0, 0, 0, 0
for i in range(n):
    x = int(input())
    if x == 2:
        D += 1
    if x == 3:
        C += 1
    if x == 4:
        B += 1
    if x == 5:
        A += 1
print(D, C, B, A)