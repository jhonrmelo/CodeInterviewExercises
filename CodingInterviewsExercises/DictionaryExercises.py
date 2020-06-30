def appearsTwice(list):
    dictNames = {}
    for name in list:
        if name in dictNames:
            return name
        else:
            dictNames[name] = 1
    return ''


def pair10(list):
    numbersSeen = {}
    for item in list:
        if(10 - item) in numbersSeen:
            print(str(10 - item) + ',' + str(item))
            return
        else:
            numbersSeen[item] = 1
    print("There is no pair that adds up to 10")
