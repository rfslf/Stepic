n, k = map(int, input().split())


def combinations(i, j):
    if j == 0 or j == i:
        return 1
    elif j > i:
        return 0
    else:
        return combinations(i - 1, j) + combinations(i - 1, j - 1)
print(combinations(n, k))
