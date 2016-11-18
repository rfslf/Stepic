import re
import sys
for line in sys.stdin:
    results = re.findall(r"((?P<cool>\d)(?P=cool){2,})", line)
    if results:
        print(line)
