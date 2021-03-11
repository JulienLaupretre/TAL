filename = "wsj_0010_sample.pos.ref"

def refToPos(filename):

    separator = "	"

    file = open(filename, "r")

    lines = file.readlines()

    file.close()

    file = open("wsj_0010_sample.pos.stanford.ref", "w")

    for line in lines:
        print(line)
        tokens = line.split(separator)
        print(tokens)

        if (tokens[0] != "."):
            file.write(tokens[0] + "_" + tokens[1].replace(" ", "").replace("\n", "") + " ")
        else:
            file.write(tokens[0] + "_" + tokens[1].replace(" ", "").replace("\n", "") + "\n")

    file.close()

refToPos(filename)