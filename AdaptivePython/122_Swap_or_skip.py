array = [int(i) for i in input().split(' ')]
x = array.pop()
swap = 0
for i in range(len(array)-1):
    if array[i] > array[i+1]:
        z = array[i+1]
        array[i+1] = array[i]
        array[i] = z
        swap += 1
print(swap)
