import requests
import re
M = []
res1 = requests.get(input())
search1 = str(res1.content)
pattern1 = r'<a[\s\w="]+href=["|\']([^"|^\']*)["|\']'
match1 = re.findall(pattern1, search1)
pattern2 = r'^(?:https://|http://|ftp://)?([\w\d\-.]+)[:\d]?[/]?[/\w\d.]*'
for i in match1:
    match2 = re.findall(pattern2, str(i))
    if match2 != ['..']:
        M.extend(match2)
M = list(set(M))
M.sort()
for j in M:
    print(j)
