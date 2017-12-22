data = ""
with open("day7data.txt") as f:
    data = f.read()

datalist = data.split('\n')  # splits data into individual lines
rootStringList = []  # list to contain only root towers

for i in range(0, len(datalist)):
    if len(datalist[i].split()) > 2:
        rootStringList.append(datalist[i])

rootList = []  # list to contain only roots

for i in range(0, len(rootStringList)):
    rootList.append(rootStringList[i].split()[0])

childList = []

for i in range(0, len(rootStringList)):
    tmp = rootStringList[i].split()
    assert isinstance(tmp, list)
    tmp.pop(0)
    tmp.pop(0)
    tmp.pop(0)
    for j in range(0, len(tmp)):
        childList.append(tmp[j].rstrip(','))

for i in range(0, len(rootList)):
    if rootList[i] not in childList:
        print(rootList[i])
        rootList[i]