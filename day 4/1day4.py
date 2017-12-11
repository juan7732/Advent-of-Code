data = ""
with open("day4data.txt") as f:
    data = f.read()

passwordList = data.split("\n")

def isValid(a):
    phraseDict = {}
    phraseList = a.split()
    for i in range(0, len(phraseList)):
        phraseDict[phraseList[i]] = i
    return len(phraseList) == len(phraseDict)

mySum = 0
for password in range(0, len(passwordList)):
    if isValid(passwordList[password]):
        mySum += 1

print(str(mySum))
