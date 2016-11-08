import re
import sys

R = str()
for line in sys.stdin:
    pattern = "\W+"
    R += line
    result = re.sub(pattern, " ", R)

print(result)
