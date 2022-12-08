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

#checks if all elements in 2d list are equal length
def determine_length_equality(twoDList):
    equality = True
    if len(twoDList)>1:
        length = len(twoDList[0])
        for element in twoDList:
            if len(element)!=length:
                equality = False
    return equality
def loop_thru_str(string):
    for char in string:
        print(char)
    return
def staircase(symbol,length):
    for i in range(1,length+1):
        print(symbol*i)
    return
def both_divisions(a,b):
    return a/b, a//b, a/b == a//b
def twoDToOneD(twoDList):
    new_list = []
    for element in twoDList:
        for i in element:
            new_list.append(i)
    return new_list
