hand = [[i[:-1], i[-1:]] for i in input().split(' ')]
trump = input()
for j in hand:
    if j[0] == 'J':
        j[0] = 11
    elif j[0] == 'Q':
        j[0] = 12
    elif j[0] == 'K':
        j[0] = 13
    elif j[0] == 'A':
        j[0] = 14
    else:
        j[0] = int(j[0])
if hand[0][1] == hand[1][1]:
    if hand[0][0] > hand[1][0]:
        print("First")
    else:
        print("Second")
else:
    if hand[0][1] == trump:
        print("First")
    elif hand[1][1] == trump:
        print("Second")
    else:
        print('Error')
