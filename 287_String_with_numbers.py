string = [i for i in input().split()]
su = 0

for i in string:
    if i.isdigit():
        su += int(i)
print(su)
