X = []

L = list(map(int, input().split()))

width = 0

def partialDigest(L):
    global X, width
    width = max(L)
    L.remove(width)
    X = [0, width]
    place(L, X)


def place(L, X):

    if not L:
        X.sort()
        for i in X:
            print(i, end=' ')
        print()
        return

    y = max(L)

    if issubset(y, X, L):
        X.append(y)
        removeElements(y, X, L)
        place(L, X)
        if y in X:
            X.remove(y)
        L.extend(D(y, X))

    if issubset(abs(width-y), X, L):
        X.append(abs(width-y))
        removeElements(abs(width-y), X, L)
        place(L, X)
        if abs(width-y) in X:
            X.remove(abs(width-y))
        L.extend(D(abs(width-y), X))

    return


def D(y, X):
    diff = []
    for xi in X:
        diff.append(abs(y-xi))
    return diff


def removeElements(y, X, L):
    for xi in X:
        if abs(y - xi) in L:
            L.remove(abs(y - xi))


def issubset(y, X, L):
        for xi in X:
            if abs(y-xi) not in L:
                return False
        return True


if __name__ == "__main__":
    print("Python implementation of partial digetive problem PDP on page 90.")

    partialDigest(L)