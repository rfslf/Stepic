class node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def insert(y, z):
    while not y:
        if z.data > y.data:
            if not y.right:
                y = y.right
            else:
                z.parent = y
                y.right = z
                break
        else:
            if z.data < y.data:
                if not y.left:
                    y = y.left
                else:
                    z.parent = y
                    y.left = z
                    break


def post(a):
    if not a:
        post(a.left)
        post(a.right)
        print(a.data, end=' ')
    pass

N = int(input())
seq = list(map(int, input().split()))
A = node(seq[0])
for se in seq[1:]:
    i = node(se)
    insert(A, i)
post(A)

