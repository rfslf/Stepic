N = int(input())
I = []
for i in range(N):
    l, r = map(int, input().split())
    I.append([r, l])
I.sort()
R = set()
for r, l in I:
    if any(l <= i <= r for i in R):
        continue
    else:
        R.add(r)
print(len(R))
for n in R:
    print(n, end=' ')
