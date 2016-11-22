import sys


def pr(w, n, t):
    print(w, end='\t')
    print(n, t, '1', sep=';')

for line in sys.stdin:
    word, number, tf = line.split()
    pr(word, number, tf)
