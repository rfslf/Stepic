def towers(n, i, j):
    if n:
        print(i, '-', j)
    else:
        k = 6-i-j
        towers(n-1, i, k)
        towers(1, i, j)
        towers(n-1, k, j)
towers(int(input()), 1, 3)
