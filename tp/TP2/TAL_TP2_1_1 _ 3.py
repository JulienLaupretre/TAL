import nltk
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')
from nltk import RegexpParser
nltk.download('maxent_ne_chunker')
nltk.download('words')

nltk.download('punkt')
from nltk.tokenize import word_tokenize

def nltk_pos_parse(filename):

    file = open(filename, "r")

    lines = file.readlines()

    file.close()

    file = open("wsj_0010_sample.txt.pos.nltk", "w") #question 1_1

    fileEnt = open("wsj_0010_sample.txt.ne.nltk", "w") #question 3_1

    fileEntConv = open("wsj_0010_sample.txt.ne.nltk.conv", "w") #question 3_2

    etq = {"ORGANIZATION" : "ORG", "PERSON" : "PERS", "LOCATION" : "LOC", "DATE" : "MISC",
     "TIME" : "MISC", "MONEY" : "MISC", "PERCENT" : "MISC", "FACILITY" : "ORG", "GPE" : "LOC"}

    for line in lines:

        tokens_tag = pos_tag(word_tokenize(line))

        for tok in tokens_tag:

            if (tok[0] == '.'):
                file.writelines(tok[0] + "	" + tok[1] + "\n\n")

            else:
                file.writelines(tok[0] + "	" + tok[1] + "\n")

           
        namedEnt = nltk.ne_chunk(tokens_tag, binary=False)
        # namedEnt.draw()        

        for subtree3 in namedEnt.subtrees():
            if(str(subtree3).startswith("(S")):

                wordGroups = (str(subtree3)[3:-1] + "\n").split("\n")

                for wordGroup in wordGroups:

                    if(wordGroup.count("/") > 1):
                        # Si il y a plusieurs "/" on doit decomposer la ligne

                        if(wordGroup.startswith("  (")): #Cas:(ORGANIZATION General/NNP Motors/NNPS)
                            ent = wordGroup.split(" ")[2][1:]
                            wordGroup = wordGroup.split(" ")[3:]
                            for word in wordGroup:
                                fileEnt.write(word.split("/")[0] + " " + ent  + "\n")

                        else: # Cas: December/NNP 10/CD ,/, 2013/CD

                            listGroup = wordGroup.split(" ")

                            for group in listGroup:
                                words = group.split("/")
                                
                                fileEnt.write(words[0] + "\t" + words[1] + "\n")

                    elif(wordGroup.startswith("  (") and not wordGroup.startswith("  (/") ):  #cas   (ORGANIZATION Hoosier	NNP)
                        #swap NE and word
                        ent = wordGroup[2:].split(" ")[0][1:]
                        word = wordGroup[2:].split(" ")[1].split("/")[0]

                        fileEnt.write(word+ "\t" + ent + "\n")
                    else: #cas classique
                        fileEnt.write(wordGroup[2:].replace("/", "\t") + "\n")

    fileEnt.close()

    # Question 2 : transformation en etiquette standard

    fileEnt = open("wsj_0010_sample.txt.ne.nltk", "r")

    lines = fileEnt.readlines()

    for line in lines:
        found = False
        for cle, val in etq.items():
            if(line.count(cle) > 0):
                found = True
                fileEntConv.write(line.replace(cle, val))

        if(not found):
            fileEntConv.write(line)

    
    fileEntConv.close()
    fileEnt.close()
    file.close()

fileIn = "wsj_0010_sample.txt"

nltk_pos_parse(fileIn)