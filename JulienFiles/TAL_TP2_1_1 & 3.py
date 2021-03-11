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
        namedEnt.draw()        

        for subtree3 in namedEnt.subtrees():
            fileEnt.write(str(subtree3))

            found = False

            for cle, val in etq.items():
                if subtree3.label() == cle:
                    found = True
                    print("ETQ")
                    print(str(subtree3))
                    print("NEW")
                    print(str(subtree3).replace(cle, val))
                    #subtree3.label() = val
                    print(subtree3.label())
                    fileEntConv.write(str(subtree3).replace(cle, val))
                
            if (not found): 
                fileEntConv.write(str(subtree3))
            
            #print (subtree3.leaves())
            
        #fileEnt.flush()
        #fileEnt.close()

        #fileEntConv.flush()
        #fileEntConv.close()

        #named_entities = [[w for w, t in elt] for elt in namedEnt if isinstance(elt, nltk.Tree)]

        #
        # print(named_entities)

        #for e in namedEnt:
        #    fileEnt.write(e[0])
    
        
        #patterns = """Compound: {<DT>?<JJ>*<NN>}}"""
        #chunker = RegexpParser(patterns)

        #output = chunker.parse(tokens_tag)


        #print("output :")
        #print(output)

        #for tok in tokens_tag:

        #    file.write(tok)
    
    file.close()

fileIn = "wsj_0010_sample.txt"

nltk_pos_parse(fileIn)