
def PrintOutput(string):
    print("OUTPUT ", string)

def LoadFile(file):
    list_ = []
    with open(file,"r") as f:
        for line in f:
            list_.append(line)
    for i in range(len(list_)-1):
        list_[i] = list_[i].strip('\n')
    return list_
            
def UpdateString(string1,string2,x):
    s = list(string1)
    s[x] = string2
    f = "".join(s)
    PrintOutput(f)
    
