string = input()
i = 0
j = 1
while i <= (len(string)-1):
    n = 1
    while 1:
        if j <= (len(string)-1):
            if string[i] == string[j]:
                n += 1
                j += 1
            else:
                break
        else:
            break
    if n != 1:
        print(n, end='')
    print(string[i], end='')
    i = j
    j += 1

