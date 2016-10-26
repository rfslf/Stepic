# put your python code here
import re
import sys
for line in sys.stdin:
#std = ['777','333','234','12','111333','1']
#for line in std:
    results = re.findall(r"((?P<cool>\d)(?P=cool){2,})", line)
    if results:
        print(line)
