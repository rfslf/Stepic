N = int(input())
Ranges = []
P = []
for n in range(N):
    l, r = map(int, input().split())
    Ranges.extend([[l, 'l'], [r, 'r']])
Ranges.sort()
P = []
paint = 0
for i in Ranges:
    if paint == 0:
        if i[1] == 'l':
            paint += 1
            P.append(i[0])
    elif paint == 1:
        if i[1] == 'l':
            paint += 1
            P.append(i[0])
        else:
            paint -= 1
            P.append(i[0])
    else:
        if i[1] == 'l':
            paint += 1
        else:
            paint -= 1
            if paint == 1:
                P.append(i[0])
def range(L):
    count = 0
    i = 0
    while i < len(L)-1:
        count += (L[i+1] - L[i])
        i += 2
    return count

print(range(P))
