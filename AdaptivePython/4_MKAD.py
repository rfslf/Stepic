V = int(input())
T = int(input())
S = 109
if V >= 0:
    print((V*T) % S)
if V < 0:
    print((109+V*T) % S)