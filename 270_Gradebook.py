N = int(input())
book = []
for i in range(N):
    name, surname, a, b, c = [i for i in input().split()]
    summa = int(a) + int(b) + int(c)
    book.append([summa, -i, name, surname])
book.sort(reverse=True)
for i in book:
    print(i[2], i[3])
