# put your python code here
# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
# У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
# <имя класса> : <количество потомков> Выводить классы следует в лексикографическом порядке.

#Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

from collections import defaultdict
import json
cdict = {}
cnames = []
jsin = input()
clist = json.loads(jsin)

for d in clist:
    cdict[d['name']] = set(d['parents'])
    cnames.append(d['name'])
csort = sorted(cnames)

newgraph = defaultdict(set)
for x, adj in cdict.items():
    for y in adj:
        newgraph[y].add(x)


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
    # перебор по вершинам в странице имен вершин
        vertex = stack.pop()
        # vertex - заберем вершину Ы с конца страницы всех вершин
        if vertex not in visited:
            # если вершина Ы не в множестве посещенных вершин то
            visited.add(vertex)
            # в множество посещенных вершин добавить вершину Ы
            stack.extend(graph[vertex] - visited)
            # расширить страницу на все смежные вершины за минусом уже посещенных
    return visited

for i in csort:
    print(i, ':', len(dfs(newgraph, i)))
