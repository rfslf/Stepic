eyes = ":", ";", ">:"
nose = "-", ""
mouth = "{", "}", "[", "]", "(", ")", "p"
string = str(input())
s = string[-1]
I, J, K = 0, 0, 0
m = False
e = False
for i in range(1, len(string) + 1):
    if string[-i] in mouth and string[-i] == s:
        m = True
    else:
        I = i
        break

if string[-I] == "-":
    J = len(string) - I - 1
else:
    J = len(string) - I

if J == 1 and string[0] == '>' and string[1] == ':':
    e = True
elif J == 0 and (string[0] == ':' or string[0] == ';'):
    e = True
else:
    e = False

if m and e:
    print(1)
else:
    print(0)
