import re
import sys
string_num = 1
pattern = re.compile(r'\s*([a-zA-Z_]\w*) = \S')
#with open('text.txt', 'r') as txt:
#    for line in txt:
for line in sys.stdin:
    result = pattern.findall(line)
    if result:
        M = result[0]
        print(string_num, end=' ')
        print(M)
    string_num += 1
