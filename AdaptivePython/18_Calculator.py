a = float(input())
b = float(input())
opr = input()
if opr == "+":
    print(a+b)
if opr == "-":
    print(a-b)
if opr == "/":
    if b == 0:
        print("Division by 0!")
    else:
        print(a/b)
if opr == "*":
    print(a*b)
if opr == "mod":
    if b == 0:
        print("Division by 0!")
    else:
        print(a % b)
if opr == "pow":
    print(a**b)
if opr == "div":
    if b == 0:
        print("Division by 0!")
    else:
        print(a//b)