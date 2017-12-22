data = ""

with open("day8data.txt") as f:
    data = f.read()

instructionList = data.split('\n')

registerDict = {}


def executeLogic(operator, register, logicTester):
    val = 0
    try:
        val = registerDict[register]
    except KeyError:
        registerDict[register] = 0

    if operator == "==":
        return val == logicTester

    elif operator == '!=':
        return val != logicTester

    elif operator == '<':
        return val < logicTester

    elif operator == '>':
        return val > logicTester

    elif operator == '>=':
        return val >= logicTester

    elif operator == '<=':
        return val <= logicTester


def changeRegister(register, modifier, incrementor):
    val = 0
    try:
        val = registerDict[register]
    except KeyError:
        registerDict[register] = 0
    if modifier == 'inc':
        val += incrementor
        registerDict[register] = val
    elif modifier == 'dec':
        val -= incrementor
        registerDict[register] = val


for i in range(0, len(instructionList)):
    tmp = instructionList[i].split()
    firstRegister = tmp[0]
    INCorDEC = tmp[1]
    modifier = int(tmp[2])
    secondRegister = tmp[4]
    logic = tmp[5]
    logicTester = int(tmp[6])

    if executeLogic(logic, secondRegister, logicTester):
        changeRegister(firstRegister, INCorDEC, modifier)
    else:
        pass


print(str(max(registerDict.values())))
