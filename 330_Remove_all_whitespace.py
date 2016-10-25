import re

In_str = str(input())
Out_str = re.sub('[ \t]+(?=[\.,!?\);:\"\'-])', '', In_str)
print(Out_str)
