from nltk import pos_tag
from nltk import RegexpParser

# text ="learn php from guru99 and make study easy".split()

fileIn = open("wsj_0010_sample.txt", "r")

lines = fileIn.readlines()
fileIn.close()

# for line in lines:
#     word = line.split("\t")

fileOut = open("wsj_0010_sample.txt.chk.nltk", "w")

listNomFiltre = ["(Adjectif-Nom", "(Nom-Nom", "(Adjectif-Nom-Nom", 
            "(Adjectif-Adjectif-Nom", "(Déterminant-Adjectif-Nom"]

listPatternFiltre = ["""Adjectif-Nom: {<JJ><NN>}""",
            """Nom-Nom: {<NN><NN>}""", 
            """Adjectif-Nom-Nom: {<JJ><NN><NN>}""", 
            """Adjectif-Adjectif-Nom: {<JJ><JJ><NN>}""",
             """Déterminant-Adjectif-Nom: {<DT>?<JJ>*<NN>}"""]

for pat in listPatternFiltre:
    for line in lines:
        # print("After Split:",line.split())
        tokens_tag = pos_tag(line.split())
        # print("After Token:",tokens_tag)
        patterns= pat
        chunker = RegexpParser(patterns)
        # print("After Regex:",chunker)
        output = chunker.parse(tokens_tag)
        # print("After Chunking",output)

        # print("LINE : ")
        for subtree3 in output.subtrees():
            # print("TREE : ")
            # print(str(subtree3))
            for nom in listNomFiltre:
                if(str(subtree3).startswith(nom)):
                    print(str(subtree3))
                    fileOut.write(str(subtree3) + "\n")


fileOut.close()