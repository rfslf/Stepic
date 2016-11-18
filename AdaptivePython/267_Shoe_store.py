size = int(input())
current_size = size
count = 0
N = int(input())
if N != 0:
    shoes = [int(i) for i in input().split()]
    shoes.sort()
    On = False

    for i in shoes:
        if i >= size and not On:
            On = True
            current_size = i
            count += 1
        elif i >= current_size + 3:
            count += 1
            current_size = i
print(count)
