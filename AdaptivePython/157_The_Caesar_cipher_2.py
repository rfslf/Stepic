n = int(input())
w = input()
print('Result: "', end='')
for i in w:
    q = ord(i)-128512
    r = (q+n) % 80 + 128512
    print(chr(r), sep='', end='')
print('"')
