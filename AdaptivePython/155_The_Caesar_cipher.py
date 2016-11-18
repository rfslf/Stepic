s = ' abcdefghijklmnopqrstuvwxyz'
n = int(input())
w = input()
print('Result: "', end='')
for i in w.strip():
    q = s.index(i)
    r = (q+n) % len(s)
    print(s[r], sep='', end='')
print('"')
