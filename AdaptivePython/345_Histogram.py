import numpy
Sepal_len = list()
with open("dataset_30642_11.txt", "r") as inpu:
    for line in inpu:
        string = line.split('\t')
        Sepal_len.append(float(string[0]))
# print(Sepal_len)
hist, bin_edges = numpy.histogram(Sepal_len, bins=10, density=False)
print(hist)
