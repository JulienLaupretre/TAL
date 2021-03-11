fileIn = open("pos_reference.txt.lima", "r")

lines = fileIn.readlines()

fileIn.close()

fileOut = open("pos_test.txt", "w")

for line in lines:
    # print(line)
    word = line.split("\t")
    print(word)
    fileOut.write(word[0] + " ")

fileOut.close()