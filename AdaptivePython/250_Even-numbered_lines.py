with open("text.txt", "r") as i, open("answer.txt", "w") as w:
    lin=1
    for line in list(i):
        if lin % 2 == 0:
            w.write(line)
            lin += 1
        else:
            lin += 1