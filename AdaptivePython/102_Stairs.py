N = int(input())
stairs = [int(i) for i in input().split()]


def staircase(stairs):
    cost = [0 for i in range(N)]
    cost[0] = stairs[0]
    cost[1] = max(stairs[1]+cost[0], stairs[1])
    if len(stairs) > 2:
        for i in range(2, N):
            cost[i] = max(cost[i-1] + stairs[i], stairs[i] + cost[i-2])
    return cost[-1]
if len(stairs) > 1:
    print(staircase(stairs))
else:
    print(stairs[0])
