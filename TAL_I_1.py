fileIn = open("pos_reference.txt.lima", "r")

lines = fileIn.readlines()

fileIn.close()

fileOut = open("pos_test.txt", "w")

for line in lines:
    # print(line)
    word = line.split("\t")
    # print(word)
    if (word[0] == "\n"):
        fileOut.write(word[0])
    else:
        fileOut.write(word[0] + " ")
fileOut.close()