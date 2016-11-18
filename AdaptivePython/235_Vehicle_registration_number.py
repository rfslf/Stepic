import re
match = re.match('^[A|B|E|K|M|H|O|P|C|T|Y|X]\d{3}[A|B|E|K|M|H|O|P|C|T|Y|X]{2}$', input())
print("Yes") if match else print('No')
