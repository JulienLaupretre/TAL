fileIn = open("pos_reference.txt.lima", "r")
lines = fileIn.readlines()
fileIn.close()

# Creation du dictionnaire LIMA -> PTB
filePTB = open("POSTags_LIMA_PTB_Linux.txt", "r")
linesPTB = filePTB.readlines()
filePTB.close()
etsPTB = {}
for line in linesPTB:
    etsPTB[line.split()[0]] = line.split()[1]

# Creation du dictionnaire PTB -> Univ
fileUniv = open("POSTags_PTB_Universal_Linux.txt", "r")
linesUniv = fileUniv.readlines()
fileUniv.close()
etsUniv = {}
for line in linesUniv:
    etsUniv[line.split()[0]] = line.split()[1]

fileOut = open("pos_reference.txt.univ", "w")

for line in lines:
    word = line.split("\t")

    if(len(word)>1):
        newLine = line.replace(word[1].replace("\n",""), etsUniv[etsPTB[word[1].replace("\n","")]])
        fileOut.write(newLine)
    else:
        fileOut.write(line) # Cas EOF

fileOut.close()

print("convertion lima -> terminée")