def read_names(fh,name):
    x=fh.readline()
    while (x!=name+"\n" and x!=""):
        print(x)
        x=fh.readline()
    return