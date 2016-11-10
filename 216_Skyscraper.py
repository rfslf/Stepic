N = int(input())
for i in range(N):
    if sum([n for n in range(1, i+1)]) >= N-1:
        print(i)
        break
