x = input()
n = x.count('A')
y = round(n/((len(x)+1)/2), 2)
if len(str(y)) == 3:
    print(str(y)+'0')
else:
    print(y)