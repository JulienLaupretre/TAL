def toCoNLL(filename):
    fileSource = open(filename, "r", encoding='UTF8')
    fileDest = open(filename + ".modif", "w")
    for line in fileSource:
        lnS = line.split("	")
        print(lnS[0])
        if len(lnS)> 1 and lnS[0] != ".":
            newLine = lnS[0] + "_" + lnS[1].replace("\n", "").replace(" ","") + " "
            fileDest.write(newLine)
        elif len(lnS)> 1:
            fileDest.write("\n")


toCoNLL("C:/Users/Dell/Desktop/Projets_ET5/TAL/TP_2/wsj_0010_sample.txt.pos.univ.ref")