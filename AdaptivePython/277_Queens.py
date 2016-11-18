Beat = False
line = range(8)
Board = [[0 for i in line] for j in line]

for _ in line:
    x, y = map(int, input().split())
    Board[x-1][y-1] = 1

for i in line:
    if sum([j for j in Board[i]]) > 1: # горизонталь
        Beat = True
        break
    elif sum([Board[j][i] for j in line]) > 1: #вертикаль
        Beat = True
        break
    elif sum([Board[i - j][j] for j in range(i + 1)]) > 1 or sum([Board[7 - i + j][7 - j] for j in range(i+1)]) > 1: #/
        Beat = True
        break
    elif sum([Board[j][7 - i + j] for j in range(i + 1)]) > 1 or sum([Board[7 - j][i - j] for j in range(i + 1)]) > 1: #\
        Beat = True
        break
if Beat:
    print("YES")
else:
    print("NO")
