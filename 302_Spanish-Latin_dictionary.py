n = int(input())
DIC = dict()
all_words = list()
for i in range(n):
    span, lat = input().split(' - ')
    words = lat.split(', ')
    for j in words:
        if not DIC.get(j):
            DIC[j] = span
            all_words.append(j)
        else:
            x = DIC.get(j)
            if type(x) == str:
                DIC[j] = [x, span]
            else:
                x.append(span)
                DIC[j] = x
all_words.sort()

print(len(all_words))
for i in all_words:
    if type(DIC[i]) == str:
        print('{} - {}'.format(i, DIC[i]))
    else:
        y = DIC[i]
        y.sort()
        print(i, '- ', end='')
        z = len(y)
        for k in range(z-1):
            print(y[k], end=', ')
        print(y[-1])
