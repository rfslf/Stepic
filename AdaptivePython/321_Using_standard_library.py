import re
with open('C:\\1.json', 'r') as inbox:
    json_in = inbox.read()
result = re.findall('\"foo\":(\d)+', json_in)
print(result)
