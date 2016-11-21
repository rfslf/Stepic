import sys
from collections import OrderedDict
D = OrderedDict()
for line in sys.stdin:
    key, value = line.split()
    if key in D:
        D[key][0] += int(value)
        D[key][1] += 1
    else:
        D[key] = [int(value), 1]
for ke in D:
    print(ke, int(D[ke][0]/D[ke][1]), sep='\t')
