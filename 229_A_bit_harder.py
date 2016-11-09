import re
import sys
string_num = 1
pattern = re.compile('\s*([a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*)((?: *, *[a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*)*) = ')

for line in sys.stdin:
    result = pattern.match(line)
    st = ''
    if result:
        M = result.groups()
        print(string_num, end=' ')
        for m in M:
            st += m.strip()
        M = st.split(', ')
        for i in M:
            print(i.strip(), end=" ")
        print()
    string_num += 1
