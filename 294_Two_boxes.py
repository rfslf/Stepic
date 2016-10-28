import itertools as it
First, Second = [], []
for i in First, Second:
    for _ in range(3):
        i.append(int(input()))


def compare(F, S):
    sizes = []
    for z in zip(F, S):
        if z[0] > z[1]:
            sizes.append(1)
        elif z[0] < z[1]:
            sizes.append(2)
        else:
            sizes.append(0)
    return sizes

Turns = it.permutations(First, 3)
for i in Turns:
    size = compare(i, Second)
    if size == [0, 0, 0]:
        print('Boxes are equal')
        break
    if 1 not in size:
        print('The first box is smaller than the second one')
        break
    elif 2 not in size:
        print('The first box is larger than the second one')
        break
else:
    print('Boxes are incomparable')
