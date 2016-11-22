from urllib.request import urlopen
import numpy as np

filename = input()
f = urlopen(filename)
source = np.loadtxt(f, delimiter=',', skiprows=1)
print(np.mean(source, axis=0))
