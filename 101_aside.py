'''
собирает максимально тяжелый рюкзак и показывает что именно надо положить
'''


W, n = map(int, input().split())
Ws = list(map(int, input().split()))
A = [[0 for i in range(W+1)] for j in range(n+1)]
ans = []


def BP(W, n, Ws):
    global A
    # от 1 до N, рассчитаем на каждом шаге d(i,c), для c от 0 до W, по рекуррентной формуле:
    for i in range(1, n+1):
        for c in range(W+1):
            if c < Ws[i-1]:
                A[i][c] = A[i - 1][c]
            else:
                A[i][c] = max((A[i - 1][c]), (A[i - 1][c - Ws[i-1]] + Ws[i-1]))
    return A[-1][-1]


def findAns(k, s):
    global A
    global ans
    if A[k][s] == 0:
        pass
    elif A[k - 1][s] == A[k][s]:
        return findAns(k - 1, s)
    else:
        ans.append(k-1)
        return findAns(k - 1, s - Ws[k-1])


x = BP(W, n, Ws)
print(A)
print(x)
findAns(n, W)
print(ans)
