n = int(input())
if n//1000 == n % 10 and n % 1000//100 == n % 1000 % 100//10:
    print('1')
else:
    print('0')