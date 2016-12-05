x = (input().split())
a = int(x[0])
b = int(x[1])
for i in range(a, b+1):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    else:
        print(i)