def check(word):
    counter = 0
    for l in word:
        if l.isupper():
            counter += 1
            if counter > 1:
                return False
    return bool(counter)

err = 0
D = {}
n = int(input())

for i in range(n):
    words = input()
    D[words] = words.lower()

D_val = set(D.values())

try:
    text = input().split()

    for word in text:
        if (word in D) or (check(word) and word.lower() not in D_val):
            continue
        else:
            err += 1
    print(err)
except EOFError:
    print(0)
