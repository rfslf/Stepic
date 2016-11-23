with open("text.txt", "r") as i, open("answer.txt", "w") as w:

    for line in reversed(list(i)):
        w.write(line)