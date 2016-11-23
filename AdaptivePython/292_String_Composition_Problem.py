n = int(input())
word = input()

with open("answer.txt", "w") as out:  
    for i in range(len(word) - n + 1):
        out.write(word[i:i+n] + '\n')