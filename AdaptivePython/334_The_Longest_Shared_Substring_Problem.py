import re
str1 = input()
str2 = input()
if len(str1) > len(str2):
    str1, str2 = str2, str1  # str2 always more than str1
out = False
for i in range(len(str1), 0, -1):
    for j in range(len(str1)-i):
        sample = str1[0+j: i+j]
        search = re.search(sample, str2)
        if search:
            print(sample)
            out = True
            break
    if out:
        break


def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]
print(longest_common_substring(str1, str2))