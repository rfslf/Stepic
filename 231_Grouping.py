import re
import sys
i = 1
for line in sys.stdin:
    Val = re.findall("(\w+) = ", line)
    if Val:
        print(i, Val[0])
    i += 1
