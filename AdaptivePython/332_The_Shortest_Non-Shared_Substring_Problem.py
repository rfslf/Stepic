str2 = input()
str1 = input()
out = False
for i in range(len(str2)):
    for j in range(len(str2)-i):
        if str2[j:j+i] not in str1:
            print(str2[j:j+i])
            out = True
            break
    if out:
        break
