def filter_positive(x):
    y = []
    for i in x:
        if int(i) > 0:
            y.append(i)
    return y
