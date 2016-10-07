W, n = map(int, input().split())
Ws = list(map(int, input().split()))

def BP(W, n, Ws):
    A = [[0 for i in range(W+1)] for j in range(n)]

    #от 1 до N, рассчитаем на каждом шаге d(i,c), для c от 0 до W, по рекуррентной формуле:
    for i in range(0, n):
        for c in range(W+1):
            if c < Ws[i]:
                A[i][c] = A[i-1][c]
            else:
                A[i][c] = max((A[i-1][c]), (A[i-1][c - Ws[i]] + Ws[i]))
    return A[W+1][-1]

print(BP(W, n, Ws))