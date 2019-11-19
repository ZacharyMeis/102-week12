
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
            
