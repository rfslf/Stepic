OUT = []
string = str()


def DEC(n, L):
    if not n:
        strng = list()
        strng.append(L[1])

        for i in L[2:]:
            strng.append(i)
        OUT.append(strng[::-1])
    else:
        if n >= L[len(L) - 1]:
            for i in range(max(1, L[len(L)-1]), n + 1):
                DEC(n - i, L + [i])
n = int(input())
DEC(n, [0])
OUT.sort()
for out in OUT:
    for i in out[0:-1]:
        print(i, end=' ')
    print(out[-1])
