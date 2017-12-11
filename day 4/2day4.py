data = ""
with open("day4data.txt") as f:
    data = f.read()

passwordList = data.split("\n")

def is_unique_length(a):
    # input is list of passphrases
    lengthDict = {}
    for i in range(0, len(a)):
        lengthDict[len(a[i])] = i
    return len(lengthDict) == len(a)


def sort_each(a):
    # input is list of passphrases
    # output is list of passphrases uniquely sorted
    sortedList = a.split()
    for i in range(0, len(sortedList)):
        sortedList[i] = "".join(sorted(sortedList[i]))
    return sortedList


def isValid(a):
    # from part 1
    phraseDict = {}
    for i in range(0, len(a)):
        phraseDict[a[i]] = i
    return len(a) == len(phraseDict)


def is_anagram_free(a):
    # splits the passPhrase into list of each individual word
    passPhrase = a.split()
    if is_unique_length(passPhrase):
        return True
    else:
        return isValid(sort_each(a))

mySum = 0
for password in range(0, len(passwordList)):
    if is_anagram_free(passwordList[password]):
        mySum += 1

print(str(mySum))