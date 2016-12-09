w = int(input())
if w < 10:
    print("0")
else:
    v = w % 100
    print(v//10)