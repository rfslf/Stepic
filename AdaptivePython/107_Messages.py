n = input()
messages = 1
l = 1
dlinna = len(n)

def message(x):
    a, b = 1, 1
    for i in range(x):
        a, b = b, a+b
    return a

for i in range(dlinna-1):
    if n[i] == '1':
        l += 1
    elif n[i] == '2':
        if n[i+1] in ['0', '1', '2', '3', '4', '5', '6']:
            l += 1
    else:
        messages *= message(l)
        l = 1
#    print(n[i], l, messages)
if l != 1:
    messages *= message(l)
print(messages)