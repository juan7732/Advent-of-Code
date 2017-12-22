data = ""

with open("day9data.txt") as f:
    data = f.read()

i = 0
isTrash = False
trashCount = 0
isScore = False

while i < len(data):
    if isTrash:
        if data[i] == '!':
            i += 2
        elif data[i] == '>':
            isTrash = False
        else:
            i += 1
            trashCount += 1
    else:
        if data[i] == '!':
            i += 1
        elif data[i] == "<":
            isTrash = True
        i += 1

print(trashCount)