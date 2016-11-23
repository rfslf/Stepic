import re

str1 = input()
out = False

for i in range(len(str1)-1, 1, -1):
    for j in range(0, len(str1)-i):
        patt = str1[j:j+i]
        RE = re.findall(patt, str1)
        if len(RE) >= 2:
            print(RE[0])
            out = True
            break
    if out:
        break
