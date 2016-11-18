import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\bcat\b', line) or re.search(r'\scat\s', line) or re.search(r'\Wcat\W', line): # whAAAt is this?
        print(line)
