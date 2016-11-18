import urllib
from urllib import request
import numpy as np

fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

# here goes your solution
qwe = np.linalg.lstsq([[1]+[d[i] for i in range(1, len(d))] for d in data], [d[0] for d in data])[0]
for i in qwe:
    print(i, end=' ')
