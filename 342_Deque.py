deque = list()
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == 1:
        deque.insert(0, b)
    elif a == 3:
        deque.append(b)
    elif a == 2:
        try:
            x = deque.pop(0)
        except IndexError:
            if b != -1:
                print("NO")
                break
        else:
            if x != b:
                print("NO")
                break
    else:
        try:
            y = deque.pop()
        except IndexError:
            if b != -1:
                print("NO")
                break
        else:
            if y != b:
                print("NO")
                break
else:
    print("YES")
