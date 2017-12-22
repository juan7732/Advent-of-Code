data = ""

with open("day9data.txt") as f:
    data = f.read()

scoreMultiplier = 1
i = 0
isTrash = False
score = 0
openScore = 0
isScore = False

while i < len(data):
    if isTrash:
        if data[i] == '!':
            i += 2
        elif data[i] == '>':
            isTrash = False
        else:
            i += 1
    else:
        if data[i] == '!':
            i += 1
        elif data[i] == "<":
            isTrash = True
        elif data[i] == '{':
            openScore += 1
            isScore = True
        elif data[i] == '}' and openScore > 0:
            score += openScore
            openScore -= 1
        i += 1

print(score)