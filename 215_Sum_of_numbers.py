def func(s):
    x = int(input())
    s += x
    if not x:
        print(s)
    else:
        func(s)
func(0)
