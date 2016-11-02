S = []
while True:
    x = int(input())
    if not x:
        break
    else:
        S.append(x)

def max_srch(List):
    '''Возвращает список с позициями в которых находятся максимумы входного списка'''
    M = [] # Максимумы
    for i in range(1, len(List)-1):
        if List[i-1] < List[i] and List[i] > List[i+1]:
            M.append(i)
    return M
ans = len(max_srch(S))
print(ans)
