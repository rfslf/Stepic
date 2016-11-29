x = input().split('.')
if len(x) == 4 and x[0].isdigit() and x[1].isdigit() and x[2].isdigit() and x[3].isdigit():
    if 0 <= int(x[0]) <= 255 and 0 <= int(x[1]) <= 255 and 0 <= int(x[2]) <= 255 and 0 <= int(x[3]) <= 255:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
# Shame for this code
