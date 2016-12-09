Y = int(input())
if (Y % 400) == 0:
    print("Leap")
else:
    if (Y % 100) == 0:
        print("Regular")
    elif (Y % 4) == 0:
        print("Leap")
    else:
        print("Regular")