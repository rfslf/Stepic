import sys
import re
count = 0
line = sys.stdin.read()
count += len(re.findall(r'you', line))
print(count)
