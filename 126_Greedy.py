# put your python code here
N = int(input())
Frts = list(map(int, input().split()))
KO = int(input())

class basket:
    def __init__(self, frts, ko):

        self.heap = frts
        self.ko = ko

    def pick(self):
        self.heap.sort()
        count = 0
        picks = []
        while self.heap:
            x = self.heap.pop()
            if count + x <= self.ko:
                count += x
                picks.append(x)
            else:
                self.heap.append(x)
                break
        return picks

    def put(self, bitten):
        self.heap.append(bitten)
        pass

X = basket(Frts, KO)

times = 0
while X.heap:
    Y = X.pick()
    times += 1
    for i in Y:
        if i == 1:
            continue
        elif i % 2 == 0:
            X.put(i//2)
        else:
            X.put((i-1)//2)
print(times)
