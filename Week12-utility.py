
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
    
def FindWordCount(l,s):
    x = 0
    for i in range(len(l)):
        y = l[i].split()
        for i in range(len(y)):
            if y[i].lower() == s.lower():
                x += 1
    return x

def ScoreFinder(list1,list2,s):
    x = -1
    for i in range(len(list1)):
        if list1[i].lower() == s.lower():
            x += list2[i] + 1
    if x == -1:
        print("OUTPUT player not found")
    else:
        print("OUTPUT",s,"got a score of",x)

def Union(s,g):
    b = []
    e = []
    for i in range(len(s)):
        b.append(s[i])
    for i in range(len(g)):
        b.append(g[i])
    for i in b: 
        if i not in e: 
            e.append(i)
    return e

def Intersection(s,g):
    b = []
    for i in range(len(s)):
        if s[i] in g:
            b.append(s[i])
    return b
            
