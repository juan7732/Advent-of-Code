data = ""
with open("1day5data.txt") as f:
    data = f.read()

data = data.split("\n")
for i in range(0, len(data)):
    data[i] = int(data[i])


def cycle(data):
    i = 0
    previ = 0
    stillInLoop = True
    steps = 0
    while stillInLoop:
        if i > (len(data) - 1):
            break
        previ = i
        i += data[i]
        if data[previ] < 3:
            data[previ] += 1
        else:
            data[previ] += -1
        steps += 1
    return steps


print(str(cycle(data)))
