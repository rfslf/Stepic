S = []
while True:
    x = int(input())
    if x == 0:
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


def min_dstn(List):
    if len(List) < 2:
        print(0)
        pass
    else:
        global S
        m = len(S)
        for i in range(len(List)-1):
            dist = List[i+1] - List[i]
            if dist < m:
                m = dist
        return m

ans = min_dstn(max_srch(S))
if ans:
    print(ans)
