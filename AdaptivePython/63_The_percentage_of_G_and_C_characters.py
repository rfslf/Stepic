genome = input()
cnt = 0
count = 0
for letter in genome:
    count += 1
    if letter=='C' or letter=='c' or letter=='G' or letter =='g':
        cnt += 1
print(cnt*100/count)