import re
def toUniv(filename):
    pos_tag = open('C:/Users/Dell/Desktop/Projets_ET5/TAL/TP_2/POSTags_PTB_Universal_Linux.txt', "r", encoding='UTF8')
    dic = {}
    for line in pos_tag:
        lineSplit = re.split('\s+', line)
        dic[lineSplit[0]] = lineSplit[1]
    pos_tag.close()

    filenameComp = filename.split("/")
    finalLink = filenameComp[len(filenameComp)-1].split(".")

    newFilename = finalLink[0] + "." + finalLink[1] + "." + finalLink[2] + ".univ."+ finalLink[3]
    file = open(filename, "r", encoding='UTF8')
    newfile = open('C:/Users/Dell/Desktop/Projets_ET5/TAL/TP_2/' + newFilename, "w")
    for line in file:
        lnS = line.split('	')
        if(len(lnS)>1):
            """print(lnS[0])
            print(lnS[1])"""
            print(lnS[1])
            newfile.write(lnS[0] + "	" + dic[lnS[1].replace("\n", "").replace(" ","")])
            newfile.write('\n')
    file.close()
    newfile.close()


mydic = toUniv('C:/Users/Dell/Desktop/Projets_ET5/TAL/wsj_0010_sample.txt.pos.nltk')