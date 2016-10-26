import requests
import sys
import re
keyout=0
A = input()
B = input()
res1 = requests.get(A)
res2 = requests.get(B)
if res1.status_code == 200:
    search1 = str(res1.content)
    match1 = re.findall(r'<a\s+href="([^"]*)"\s*>', search1)
    for i in match1:
        if requests.get(i).status_code == 200 and keyout == 0:
            search2 = str(requests.get(i).content)
            match2 = re.findall(r'<a\s+href="([^"]*)"\s*>', search2)
            for j in match2:
                if j == B:
                    keyout = 1
                    break
        if keyout == 1: break
if keyout == 0: print('No')
if keyout == 1: print('Yes')