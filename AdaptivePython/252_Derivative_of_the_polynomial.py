import re
Dict = {}
polys = input()


def deriv(st):
    global Dict
    power = st - 1
    koe = Dict[st] * st
    if power == 1:
        if koe == 1:
            return 'x'
        elif koe == -1:
            return '-x'
        else:
            return str(koe) + '*x'
    elif power == 0:
        if koe == 1:
            return '1'
        elif koe == -1:
            return '-1'
        else:
            return str(koe)
    else:
        if koe == 1:
            return 'x^' + str(power)
        elif koe == -1:
            return '-x^' + str(power)
        else:
            return str(koe) + '*x^' + str(power)
    return

patt1 = re.compile('(-?\s*\d*\*?x\^?\d*)')
patt2 = re.compile('(-)?\s*(\d*)\*?x\^?(\d*)')

poly = patt2.findall(polys)
for i in poly:
    i = list(i)
    if i[2] == '':
        i[2] = '1'
    if i[1] == '':
        i[1] = '1'
    if int(i[2]) in Dict.keys():
        Dict[int(i[2])] += int(i[0]+i[1])
    else:
        Dict[int(i[2])] = int(i[0]+i[1])
dk = list(Dict.keys())
dk.sort(reverse=True)
print(deriv(dk[0]), end='')
for d in dk[1:]:
    p = deriv(d)
    if p[0] == '-':
        print(p, end='')
    else:
        print('+' + p, end='')
