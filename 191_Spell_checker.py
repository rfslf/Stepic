d = set()
txt = set()
count = int(input())
for i in range(count):
    d.add(input().lower())

l = int(input())
for j in range(l):
    line = input().strip().lower().split(' ')
    for text in line:
        if text not in d:
            txt.add(text)
for w in txt:
    print(w)
