money = int(input())
Coins = [int(i) for i in input().split(',')]
Coins.sort()
Coins.reverse()
number = 0
for i in Coins:
    numb = money//i
    money -= numb*i
    number += numb
    if money == 0:
        print(number)
        break
