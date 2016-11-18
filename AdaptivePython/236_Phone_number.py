import re
match = re.match('^19\d{9}$', input())
print("Yes") if match else print('No')
