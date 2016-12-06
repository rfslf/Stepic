a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(' ', '\t', end='')
for y in range(c, d+1, 1):
    print(y, '\t', end='')
print()
for x in range(a, b+1, 1):
        print(x, '\t', end='')
        for y in range(c, d+1, 1):
            print((x*y), '\t', end='')
        print()