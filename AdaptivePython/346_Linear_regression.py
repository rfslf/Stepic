import numpy as np
from sklearn.metrics import r2_score
Sepal_len = list()
petal_length, petal_width = [], []
with open("text.txt", "r") as inpu:
    for line in inpu:
        string = line.split()
        petal_length.append(float(string[2]))
        petal_width.append(float(string[3]))
        Sepal_len.append(string)

Y = np.array(petal_length)
X = np.array(petal_width)
A = np.vstack([X, np.ones(len(X))]).T
a, b = np.linalg.lstsq(A, Y)[0]
print('{:.4f}'.format(a), '{:.4f}'.format(b), end=' ')
print(r2_score(Y, a*X+b))
