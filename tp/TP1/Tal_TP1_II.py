def namedEntityOccurences(filename):
    fileSource = open(filename, "r", encoding='UTF8')
    fileDest = open("C:/Users/Dell/Desktop/Projets_ET5/TAL/projet/namedEntityOccurences.txt", "w")
    coupleWordTypeOcc = {}
    for line in fileSource:
        lnS = line.split(' ')
        for couple in lnS:
            coupleTab = couple.split('/')
            if(len(coupleTab)> 1):
                if (coupleTab[0], coupleTab[1]) not in coupleWordTypeOcc.keys():
                    coupleWordTypeOcc[(coupleTab[0], coupleTab[1])] = 1
                else:
                    coupleWordTypeOcc[(coupleTab[0], coupleTab[1])] = coupleWordTypeOcc[(coupleTab[0], coupleTab[1])] +1
    print(coupleWordTypeOcc)
    for cle in coupleWordTypeOcc.keys():
        fileDest.write(cle[0] + "	" + cle[1] + "	" + str(coupleWordTypeOcc[cle]) + "	" + str(coupleWordTypeOcc[cle]/len(
            coupleWordTypeOcc)) + "\n")

namedEntityOccurences("C:/Users/Dell/Desktop/Projets_ET5/TAL/TP1/stanford-ner-2018-10-16/wsj_0010_sample.txt.ner.stanford")