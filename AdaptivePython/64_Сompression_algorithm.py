string = input()
i = 0
j = 1
while i <= (len(string)-1):
    n = 1
    while True:
        if j <= (len(string)-1):
            if string[i] == string[j]:
                n += 1
                j += 1
            else:
                break
        else:
            break
    print(string[i], end='')
    print(n, end='')
    i = j
    j += 1