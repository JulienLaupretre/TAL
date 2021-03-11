
import re


def toUniv(filename):
    pos_tag = open('D:/selma/Documents/etudes/ET5/tal/TP_1/POSTags_PTB_Universal_Linux.txt', "r", encoding='UTF8')
    dic = {}
    for line in pos_tag:
        lineSplit = re.split('\s+', line)
        print(lineSplit[0])
        print(lineSplit[1])
        dic[lineSplit[0]] = lineSplit[1]
    pos_tag.close()

    file = open(filename, "r", encoding='UTF8')
    newfile = open(filename + ".univ", "w")
    for line in file:
        lineSplit = line.split(' ')
        for t in lineSplit:
            lnS = t.split('_')
            newfile.write(lnS[0] + "_" + dic[lnS[1].replace("\n", "")] + " ")
        newfile.write('\n')
    file.close()
    newfile.close()


mydic = toUniv('D:/selma/Documents/etudes/ET5/tal/wsj_0010_sample.txt.pos.stanford')




