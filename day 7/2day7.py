class Node:
    def __init__(self, a, b):
        self.name = a
        self.weight = b
        self.tower = []

    def add_tower(self, tower):
        self.tower.append(tower)


data = ""
with open("day7data.txt") as f:
    data = f.read()

datalist = data.split('\n')  # splits data into individual lines
towerStringList = datalist  # list to contain only programs
rootStringList = []  # list to contain only string of roots

for i in range(0, len(datalist)):
    if len(datalist[i].split()) > 2:
        rootStringList.append(datalist[i])

print(towerStringList)
print(rootStringList)
towerNodeList = []

for i in range(0, len(towerStringList)):
    tmp = towerStringList[i].split()
    name = tmp[0]
    weight = int(tmp[1].lstrip('(').rstrip(')'))
    towerNodeList.append(Node(name, weight))

for node in towerNodeList:
    print(node.name, end=" ")
