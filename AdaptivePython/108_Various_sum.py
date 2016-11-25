n = int(input())
A = [int(i) for i in input().split()]

S = {0}
for i in A:
    T = {i + j for j in S}
    S = T | S
print(len(S))