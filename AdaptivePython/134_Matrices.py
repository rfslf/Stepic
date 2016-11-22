import numpy as np

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)
y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)
del x_shape
del y_shape

# here goes your solution; X and Y are already defined!
Y = Y.transpose()
try:
    print(np.dot(X, Y))
except ValueError:
    print("matrix shapes do not match")
