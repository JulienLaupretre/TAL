def toCoNLL(filename):
    fileSource = open(filename , "r", encoding='UTF8')
    fileDest = open("../data/ne_test.txt.ne.nltk.conll", "w")
    Pred = ""
    for line in fileSource:
        lnS = ""
        if '	' in line:
            lnS = line.split('	')
        else:
            lnS = line.split(" ")
        print(len(lnS))
        if len(lnS) > 1:
            if lnS[1].replace("\n", "").replace(" ","") == "PERSON":
                if Pred == "PERSON":
                    fileDest.write(lnS[0] + "	" + "I-PERS"+ '\n')
                else:
                    fileDest.write(lnS[0] + "	" + "B-PERS"+ '\n')
                    Pred = "PERSON"

            elif lnS[1].replace("\n", "").replace(" ","") == "ORGANIZATION":
                if Pred == "ORGANIZATION":
                    fileDest.write(lnS[0] + "	" + "I-ORG"+ '\n')
                else:
                    fileDest.write(lnS[0] + "	" + "B-ORG"+ '\n')
                    Pred = "ORGANIZATION"

            elif lnS[1].replace("\n", "").replace(" ","") == "LOCATION":
                if Pred == "LOCATION":
                    fileDest.write(lnS[0] + "	" + "I-LOC"+ '\n')
                else:
                    fileDest.write(lnS[0] + "	" + "B-LOC" + '\n')
                    Pred = "LOCATION"
            else:
                Pred = "O"
                fileDest.write(lnS[0] + "	" + "O"+ '\n')
        else:
            fileDest.write(line)
    fileSource.close()
    fileDest.close()

#toCoNLL("../data/ne_test.txt.ne.nltk")