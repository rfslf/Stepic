b = input()

def Evaluate(str):
    stack = []
    pushChars, popChars = "({[", ")}]"

    for c in str:
        if c in pushChars:
            stack.append(c)
        elif c in popChars:
            if not len(stack):
                stack.append(c)
            else:
                stackTop = stack.pop()
                if stackTop in pushChars:
                    if stackTop != pushChars[popChars.index(c)]:
                        return -1
                else:
                    stack.append(stackTop)
                    stack.append(c)
        else:
            return -1
    return stack

def Finish(lst):
    a = []
    b = []
    pushChars, popChars = "({[", ")}]"
    while lst:
        c = lst.pop()
        if c in pushChars:
            balancingBracket = popChars[pushChars.index(c)]
            b.append(balancingBracket)
        elif c in popChars:
            balancingBracket = pushChars[popChars.index(c)]
            a.append(balancingBracket)
        else:
            return False
    return [a, b]

scum = Evaluate(b)
if scum != -1:
    fin = Finish(scum)
    print(''.join(fin[0]) + b + ''.join(fin[1]))
else:
    print('IMPOSSIBLE')
