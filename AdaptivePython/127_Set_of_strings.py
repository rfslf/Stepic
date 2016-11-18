import sys
rows = [line.replace('\n', '') for line in sys.stdin.readlines()]

hash = {}


def oper(string):
    global hash
    op = string[0]
    value = string[2:]
    if op == '+':
        if value in hash.keys():
            print("FAIL")
        else:
            hash[value] = 1
            print('OK')
    elif op == '-':
        if value in hash.keys():
            trash = hash.pop(value)
            print("OK")
        else:
            print("FAIL")
    else:
        if value in hash.keys():
            print("OK")
        else:
            print("FAIL")

for i in rows:
    oper(i)

