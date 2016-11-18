from functools import reduce
x = int(input())
c = reduce(lambda res, y: y(res), [f] * 1024, x)
print(c)
