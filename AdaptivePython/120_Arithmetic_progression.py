seq = [int(i) for i in input().split()]
seq.sort()
Flag = True
if len(seq) > 1:
    hop = seq[1] - seq[0]
    for i in range(1, len(seq)-1):
        if seq[i] + hop != seq[i+1]:
            Flag = False
            break
if Flag:
    print("Yes")
else:
    print("No")
