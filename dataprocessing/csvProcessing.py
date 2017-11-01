
with open('D:\\python_projects\\SpiderOne\\plosone.csv', "r", encoding='utf-8') as file:
    # print file header
    header = file.readline()
    print(header.split('|'))

    # number of papers
    count = 0
    # number of papers that contains subject
    subCount =0
    # number of abstract
    absCount = 0
    # number of introduction
    intrCount = 0
    # number of method
    metCount = 0
    # number of result
    resCount = 0
    # number of discussion
    disCount = 0
    # get number of IMRD
    imrdCount = 0
    # get number of AIMRD
    aimrdCount = 0

    for i in range(1, 189588):
        # each item is a paper from plosone
        item = file.readline().split('|')
        # print(item)

        # get paper number
        count = count + 1

        # get subject number
        if item[1] != "":
            subCount = subCount + 1
        else:
            subCount = subCount

        # get abstract number
        if item[2] != "":
            absCount = absCount + 1
        else:
            absCount = absCount

        # get introduction number
        if item[3] != "":
            intrCount = intrCount + 1
        else:
            intrCount = intrCount

        # get method number
        if item[4] != "":
            metCount = metCount + 1
        else:
            metCount = metCount

        # get result number
        if item[5] != "":
            resCount = resCount + 1
        else:
            resCount = resCount

        # get discussion number
        if item[6] != "":
            disCount = disCount + 1
        else:
            disCount = disCount

        # get imrd number
        if item[3] != "" and item[4] != "" and item[5] != "" and item[6] != "":
            imrdCount = imrdCount + 1
        else:
            imrdCount = imrdCount

        # get aimrd number
        if item[2] != "" and item[3] != "" and item[4] != "" and item[5] != "" and item[6] != "":
            aimrdCount = aimrdCount + 1
        else:
            aimrdCount = aimrdCount

    print("paper:" + " " + str(count))
    print("subject:" + " " + str(subCount))
    print("abstract:" + " " + str(absCount))
    print("introduction:" + " " + str(intrCount))
    print("method:" + " " + str(metCount))
    print("resut:" + " " + str(resCount))
    print("discussion:" + " " + str(disCount))
    print("IMRD:" + " " + str(imrdCount))
    print("AIMRD:" + " " + str(aimrdCount))
