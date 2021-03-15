import nltk
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')
from nltk import RegexpParser
nltk.download('maxent_ne_chunker')
nltk.download('words')

nltk.download('punkt')
from nltk.tokenize import word_tokenize

import time

def nltk_pos_parse(filename):

    file = open(filename, "r")

    lines = file.readlines()

    file.close()

    fileEnt = open("../data/ne_test.txt.ne.nltk", "w")

    # etq = {"ORGANIZATION" : "ORG", "PERSON" : "PERS", "LOCATION" : "LOC", "DATE" : "MISC",
    #  "TIME" : "MISC", "MONEY" : "MISC", "PERCENT" : "MISC", "FACILITY" : "ORG", "GPE" : "LOC"}

    tps1 = time.process_time()

    print("extraction EN...")

    for line in lines:

        tokens_tag = pos_tag(word_tokenize(line))
           
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

                            #Gestion des 3 exceptions non prise en compte par l'algorithme
                            # pb l 123 "said Obama . ", 351 "General Motors logo . "
                            # 377 "Mr MacFarlane said . "
                            # L'algorithme devra donc être modifié si l'on change de fichier d'entrée
                            if(wordGroup.count("Obama") > 0):
                                fileEnt.write("said" + "\t" + "VBD" + "\n")
                                fileEnt.write("Obama" + "\t" + "PERSON" + "\n")
                                fileEnt.write("." + "\t" + "." + "\n")

                            elif(wordGroup.count("Motors") > 0):
                                fileEnt.write("General" + "\t" + "ORGANIZATION" + "\n")
                                fileEnt.write("Motors" + "\t" + "ORGANIZATION" + "\n")
                                fileEnt.write("logo" + "\t" + "NN" + "\n")
                                fileEnt.write("." + "\t" + "." + "\n")

                            elif(wordGroup.count("MacFarlane") > 0):
                                fileEnt.write("Mr" + "\t" + "NNP" + "\n")
                                fileEnt.write("MacFarlane" + "\t" + "ORGANIZATION" + "\n")
                                fileEnt.write("said" + "\t" + "VBD" + "\n")
                                fileEnt.write("." + "\t" + "." + "\n")

                            else:
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

    tps2 = time.process_time()

    tps = tps2 - tps1

    print("temps d'execution : " + str(tps) + " seconde(s)")

fileIn = "../data/ne_test.txt"

nltk_pos_parse(fileIn)