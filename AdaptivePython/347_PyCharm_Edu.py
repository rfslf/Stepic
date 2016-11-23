n = int(input())
summary = 0
start = 1
for i in range(n):
    summary += start
    start *= -0.5
print(summary)
