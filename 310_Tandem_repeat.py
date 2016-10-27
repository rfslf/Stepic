import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b(\w+)\1\b"
    if re.findall(pattern, line):
        print(line)
