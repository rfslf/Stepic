import itertools
k, n = map(int, input().split())
for combo in itertools.combinations(range(n), k):
    for num in combo:
        print(num, end=' ')
    print()
