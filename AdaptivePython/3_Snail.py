H = int(input())
A = int(input())
B = int(input())
i = 1
h = 0
while True:
    h += A
    if h >= H:
        print(i)
        break
    else:
        h -= B
    i += 1