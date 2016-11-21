hand = [[i[:-1], i[-1:]] for i in input().split(' ')]
face = list()
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
    face.append(j[0])

if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
    suit = True
else:
    suit = False

face.sort()
face_set = set(face)

if face[0] == face[1] - 1 == face[2] - 2 == face[3] - 3 == face[4] - 4:
    face_val = 'Straight'
    if face[0] == 10:
        Royal = True
    else:
        Royal = False

else:
    if len(face_set) == 5:
        face_val = 'High Card'
    elif len(face_set) == 4:
        face_val = 'Pair'
    elif len(face_set) == 3:
        if face[0] == face[1] == face[2] or face[1] == face[2] == face[3] or face[2] == face[3] == face[4]:
            face_val = 'Three of a Kind'
        else:
            face_val = 'Two Pairs'
    elif len(face_set) == 2:
        if face[0] == face[1] == face[2] == face[3] or face[1] == face[2] == face[3] == face[4]:
            face_val = 'Four of a Kind'
        else:
            face_val = 'Full House'

if suit:
    if face_val == 'Straight':
        if not Royal:
            value = 'Straight Flush'
        else:
            value = 'Royal Flush'
    else:
        value = 'Flush'
else:
    value = face_val

print(value)
