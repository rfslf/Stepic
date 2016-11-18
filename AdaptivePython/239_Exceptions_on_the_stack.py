n = int(input())
stack = input().split()

m = int(input())
D = {}
for i in range(m):
    fun, e1, e2 = input().split()
    if fun in D.keys():
        D[fun][e1] = e2
    else:
        D[fun] = {e1: e2}
exept = input()
while stack:
    fun_top = stack.pop()
    if fun_top in D.keys():
        fun_ex = D[fun_top]
        if exept in fun_ex.keys():
            exept = fun_ex[exept]
            if exept == '_':
                stack.append(fun_top)
                break
            else:
                continue
        else:
            continue
    else:
        break
for i in stack:
    print(i, end=' ')
