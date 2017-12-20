data = [4,	10,	4,	1,	8,	4,	9,	14,	5,	1,	14,	15,	0,	15,	3,	5]
data1 = [0, 2, 7, 0]


def reallocate(data):
    j = 0
    maxBlock = max(data)
    for i in range(0, len(data)):
        if data[i] == maxBlock:
            data[i] = 0
            j = i + 1
            break

    while maxBlock > 0:
        if j > len(data) - 1:
            j = 0
        data[j] += 1
        maxBlock -= 1
        j += 1

    return data


memoryState = {}

stateCounter = 0
a = []
while stateCounter == len(memoryState) or stateCounter -1 == len(memoryState):
    stateCounter += 1
    data = reallocate(data)
    a = [str(d) for d in data]
    memoryState["".join(a)] = stateCounter
print(data)
print(stateCounter)

memoryState = {}

stateCounter = 0

while stateCounter == len(memoryState) or stateCounter -1 == len(memoryState):
    stateCounter += 1
    data = reallocate(data)
    a = [str(d) for d in data]
    memoryState["".join(a)] = stateCounter

print(data)
print(stateCounter - 1)