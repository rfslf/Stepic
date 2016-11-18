def Calc(N):
    steps = [50 for i in range(N+1)]
    steps[N] = 0
    next_num = [-1 for i in range(N+1)]
    for i in range(N, 1, -1):
        s = steps[i] + 1
        if i % 3 == 0 and steps[i // 3] > s:
            steps[i // 3] = s
            next_num[i // 3] = i
        if i % 2 == 0 and steps[i // 2] > s:
            steps[i // 2] = s
            next_num[i // 2] = i
        if steps[i - 1] > s:
            steps[i - 1] = s
            next_num[i - 1] = i
    print(steps[1])
    i = 1
    while i != -1:
        print(i, end=' ')
        i = next_num[i]
    pass

N = int(input())
Calc(N)