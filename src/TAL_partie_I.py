import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
import re


# fonction Question 1 Partie I
def colTotext (fichier):
    fileIn = open(fichier, "r")

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

#colTotext("../data/pos_reference.txt.lima")

#fonction Question 2  Version1 Partie I : fichier au format deux colonnes
def to_univ_tags(fichier):
    fileIn = open(fichier, "r")
    lines = fileIn.readlines()
    fileIn.close()

    # Creation du dictionnaire LIMA -> PTB
    filePTB = open("../data/POSTags_LIMA_PTB_Linux.txt", "r")
    linesPTB = filePTB.readlines()
    filePTB.close()
    etsPTB = {}
    for line in linesPTB:
        etsPTB[line.split()[0]] = line.split()[1]

    # Creation du dictionnaire PTB -> Univ
    fileUniv = open("../data/POSTags_PTB_Universal_Linux.txt", "r")
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



#fonction Question 2  Version2 Partie I : fichier format mot_tag
def to_univ_tags2(fichier):
    fileIn = open(fichier, "r")
    lines = fileIn.readlines()
    fileIn.close()

    # Creation du dictionnaire LIMA -> PTB
    filePTB = open("../data/POSTags_LIMA_PTB_Linux.txt", "r")
    linesPTB = filePTB.readlines()
    filePTB.close()
    etsPTB = {}
    for line in linesPTB:
        etsPTB[line.split()[0]] = line.split()[1]

    # Creation du dictionnaire PTB -> Univ
    fileUniv = open("../data/POSTags_PTB_Universal_Linux.txt", "r")
    linesUniv = fileUniv.readlines()
    fileUniv.close()
    etsUniv = {}
    for line in linesUniv:
        etsUniv[line.split()[0]] = line.split()[1]

    fileOut = open("pos_reference.txt.univ.modif", "w")

    for line in lines:
        word = line.split("\t")
        print(word)

        if(len(word)>1):
            newLine = word[0]+"_"+etsUniv[etsPTB[word[1].replace("\n","")]] + " "
            fileOut.write(newLine)
        else:
            fileOut.write('\n') # Cas EOF

    fileOut.close()

#to_univ_tags2("../data/pos_reference.txt.lima")


#fonction Question 3  Partie I : pos tagger nltk
def tagNltk (fichier):
    file = open(fichier, "r", encoding='UTF8')
    lines = file.readlines()
    file.close()
    newfile=open("pos_test.txt.pos.nltk", "w")

    for line in lines:
        res=nltk.pos_tag(word_tokenize(line))
        for r in res:
            newfile.write(r[0]+"_"+r[1]+" ")
        newfile.write('\n')

    newfile.close()

#tagNltk("../data/pos_test.txt")

#fonction Question 4 Partie I : nltk et stanford
def toUniv(filename):
    pos_tag = open('../data/POSTags_PTB_Universal_Linux.txt', "r", encoding='UTF8')
    dic = {}
    for line in pos_tag:
        lineSplit = re.split('\s+', line)
        dic[lineSplit[0]] = lineSplit[1]
    pos_tag.close()
    file = open(filename, "r", encoding='UTF8')
    newfile = open(filename + ".univ", "w")
    for line in file:
        lineSplit = line.split(' ')
        for t in lineSplit:
            if(t[0]!='\n'):
                lnS = t.split('_')
                ref=lnS[1]
                if (lnS[1].replace("\n", "")!= 'HYPH'):
                    newfile.write(lnS[0] + "_" + dic[ref.replace("\n", "")] + " ")
        newfile.write('\n')
    file.close()
    newfile.close()

#toUniv('../data/pos_test.txt.pos.nltk')
#toUniv('../data/pos_test.txt.pos.stanford')

