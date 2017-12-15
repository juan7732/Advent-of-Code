data = [0, 2, 7, 0]


def reallocate(data):
    j = 0
    maxBlock = max(data)
    for i in range(0, len(data)):
        if data[i] == maxBlock:
            data[i] = 0
            j = i + 1
            break

    while maxBlock > 0:
        data[j] += 1
        maxBlock -= 1
        j += 1
        if j > len(data) - 1:
            j = 0
    return data



memoryState = {}

print(data)