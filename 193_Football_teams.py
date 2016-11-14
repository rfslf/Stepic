games = int(input())
T = {}
for g in range(games):
    match = input().split(';')
    t1 = T.get(match[0])
    t2 = T.get(match[2])
    if not t1:
        T[match[0]] = {'G': 0, 'W': 0, 'E': 0, 'L': 0, 'P': 0}
    if not t2:
        T[match[2]] = {'G': 0, 'W': 0, 'E': 0, 'L': 0, 'P': 0}

    if int(match[1]) > int(match[3]):
        Ta = T[match[0]]
        Ta['P'] += 3
        Ta['W'] += 1
        Ta['G'] += 1
        Tb = T[match[2]]
        Tb['L'] += 1
        Tb['G'] += 1
    elif int(match[1]) < int(match[3]):
        Ta = T[match[0]]
        Ta['L'] += 1
        Ta['G'] += 1
        Tb = T[match[2]]
        Tb['P'] += 3
        Tb['W'] += 1
        Tb['G'] += 1
    else:
        Ta = T[match[0]]
        Ta['P'] += 1
        Ta['E'] += 1
        Ta['G'] += 1
        Tb = T[match[2]]
        Tb['P'] += 1
        Tb['E'] += 1
        Tb['G'] += 1
for line in T:
    print(line, ':', T[line].get('G'), ' ', T[line].get('W'), ' ', T[line].get('E'), ' ', T[line].get('L'), ' ',
          T[line].get('P'), sep='')
