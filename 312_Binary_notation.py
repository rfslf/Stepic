import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    if re.fullmatch(r'(^[01]+$)',line):
        subline = line
        while True:
            subline = re.sub(r'(11|00)+', "", subline)
            if subline in ["", "0"]:
                print(line)
                break
            elif subline in ["1", "01", "10", "010", "101", "0101", "1010", "01010"]:
                break
            elif not re.search(r'(00)|(11)',subline):
                subline = re.sub(r'(10101)+', "", subline)