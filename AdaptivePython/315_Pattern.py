import sys
import re
#line='What are youyou doing here?'
count = 0
for line in sys.stdin:
    count += len(re.findall(r'you', line))
print(count)
