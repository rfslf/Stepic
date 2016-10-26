# put your python code here
n = int(input())
space = {'global': {'parent': '', 'var': []}}


def create(namespace, parent):
    global space
    space[namespace] = {'parent': '', 'var': []}
    space[namespace]['parent'] = parent


def add(namespace, var):
    global space
    space[namespace]['var'].append(var)


def get(namespace, var):
    if var in space[namespace]['var']:
        return namespace
    elif namespace == 'global':
        return 'None'
    else:
        return get(space[namespace]['parent'], var)

for i in range(n):
    act, ns, obj = (i for i in input().split())
    if act == 'create': create(ns, obj)
    if act == 'add': add(ns, obj)
    if act == 'get': print(get(ns, obj))
