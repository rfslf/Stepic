import re
import sys
res = 0
for line in sys.stdin:
    results = re.findall("(y|Y)ou", line)
    res += len(results)
print(res)
