S = input()
i=0
while i < len(S):
    if S[i] == '0' and S[i+1] == '0':
        print('A', end='')
    elif S[i] == '0' and S[i+1] == '1':
        print('C', end='')
    elif S[i] == '1' and S[i+1] == '0':
        print('G', end='')
    else:
        print('T', end='')
    i += 2
