fileIn = open("../data/ne_test.txt.ne.stanford_noFormat", "r")

lines = fileIn.readlines()

fileIn.close()

fileOut = open("../data/ne_test.txt.ne.stanford", "w")

for line in lines:
    # # print(line)
    # word = line.split("\t")
    # # print(word)
    # if (word[0] == "\n"):
    #     fileOut.write(word[0])
    # else:
    #     fileOut.write(word[0] + " ")
    newLine = line.replace("/", "\t").replace(" ", "\n")
    fileOut.write(newLine)
fileOut.close()