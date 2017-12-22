from collections import defaultdict


class Node(object):
    name_index = defaultdict(list)

    def __init__(self, a, b):
        self.name = a
        self.weight = b
        Node.name_index[name].append(self)
        self.tower = []

    def add_tower(self, t):
        self.tower.append(t)

    def return_sum(self):
        mySum = 0
        mySum += self.weight
        for i in range(0, len(self.tower)):
            mySum += self.tower[i].return_sum()
        return mySum

    def print_child_list(self, k):
        if len(self.tower) == 0:
            pass
        else:
            for i in range(0, len(self.tower)):
                for m in range(0,k):
                    print("\t", end="")
                print(self.tower[i].name)
                self.tower[i].print_child_list(k + 1)

    def print_tower(self):
        print(self.name, end=":")
        for i in range(0, len(self.tower)):
            print(self.tower[i].name, end=" ")

    @classmethod
    def find_by_name(cls, n):
        return Node.name_index[n]


data = ""
with open("day7data.txt") as f:
    data = f.read()

def findRoot(datalist):
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
            return rootList[i]

datalist = data.split('\n')  # splits data into individual lines
towerStringList = datalist  # list to contain only programs
rootStringList = []  # list to contain only string of roots

for i in range(0, len(datalist)):
    if len(datalist[i].split()) > 2:
        rootStringList.append(datalist[i])

towerNodeList = []

for i in range(0, len(towerStringList)):
    tmp = towerStringList[i].split()
    name = tmp[0]
    weight = int(tmp[1].lstrip('(').rstrip(')'))
    towerNodeList.append(Node(name, weight))

for m in range(0, len(rootStringList)):
    tempList = rootStringList[m].split()
    tempList.pop(1)
    tempList.pop(1)
    for i in range(0, len(tempList)):
        tempList[i] = tempList[i].strip(",")
    for k in range(1, len(tempList)):
        Node.find_by_name(tempList[0])[0].add_tower(Node.find_by_name(tempList[k])[0])

weightList = []

for node in towerNodeList:
    if len(node.tower) > 1:
        node.print_tower()
        print(node.return_sum())
        weightList.append(node.return_sum())

Node.find_by_name(findRoot(data))[0].print_child_list(0)
for node in Node.find_by_name(findRoot(data))[0].tower[4].tower:
    print(node.name)
    print(node.return_sum())

# finished 7 part 2 by deduction, in the end argoys was wrong, simple backtrack of arqoys fixes the issue