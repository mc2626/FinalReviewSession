def read_names(fh,name):
    x=fh.readline()
    while (x!=name+"\n" and x!=""):
        print(x)
        x=fh.readline()
    return
def read_every_element(twoDList):
    for element in twoDList:
        for item in element:
            print(item)
    return
def determine_length_equality(twoDList):
    equality = True
    if len(twoDList)>1:
        length = len(twoDList[0])
        for element in twoDList:
            if len(element)!=length:
                equality = False
    return equality