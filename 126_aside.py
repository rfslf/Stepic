'''
    берутся не максимально тяжелые фрукты, а комбинации фруктов, которые весят макисмимум
'''



N = int(input())
Frts = list(map(int, input().split()))
KO = int(input())


def BP(W, n, Ws):
    A = [[0 for i in range(W + 1)] for j in range(n + 1)]
    # от 1 до N, рассчитаем на каждом шаге d(i,c), для c от 0 до W, по рекуррентной формуле:
    for i in range(1, n + 1):
        for c in range(W + 1):
            if c < Ws[i - 1]:
                A[i][c] = A[i - 1][c]
            else:
                A[i][c] = max((A[i - 1][c]), (A[i - 1][c - Ws[i - 1]] + Ws[i - 1]))
    return A


def findAns(k, s, A, ws):
    ans = []
    i = k
    j = s
    while A[i][j] != 0:
        if A[i - 1][j] == A[i][j]:
            i -= 1
        else:
            ans.append(i - 1)
            j -= ws[i - 1]
            i -= 1
    return ans

class basket:
    def __init__(self, frts, ko):

        self.heap = frts
        self.ko = ko

    def pick(self):
        self.heap.sort()
        picks = []
        bp = BP(self.ko, len(self.heap), self.heap)
        print(len(self.heap), self.ko, bp, self.heap)
        fa = findAns(len(self.heap), self.ko, bp, self.heap)
        print('fa', fa)
        for i in fa:
            picks.append(self.heap.pop(i))
        return picks


    def put(self, bitten):
        self.heap.append(bitten)
        pass

X = basket(Frts, KO)

times = 0
while X.heap:
    Y = X.pick()
    print(Y)
    times += 1
    for i in Y:
        if i == 1:
            continue
        elif i % 2 == 0:
            X.put(i//2)
        else:
            X.put((i-1)//2)
print(times)
