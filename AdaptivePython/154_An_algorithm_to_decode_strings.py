s = input()
i = 0
n = '0'
out = ''
while i < len(s):
    if s[i] in '0123456789':
        n += s[i]
        i += 1
    else:
        out += s[i] + s[i] * (int(n) - 1)
        n = '0'
        i += 1
print(out)
