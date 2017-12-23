# Circular Hash

def flip_list(length, currentPosition):
    reverseList = []
    for j in range(currentPosition, currentPosition + length):
        if j >= len(a):
            reverseList.append(a[j % len(a)])
        else:
            reverseList.append(a[j])
    o = 0
    for k in range(currentPosition, currentPosition + length):
        if k >= len(a):
            a[k % len(a)] = reverseList[len(reverseList) - 1 - o]
            o += 1
        else:
            a[k] = reverseList[len(reverseList) - 1 - o]
            o += 1
    # print(a)


a = list(range(0, 256))
currentPositionOut = 0
skipSize = 0

pattern = [88, 88, 211, 106, 141, 1, 78, 254, 2, 111, 77, 255, 90, 0, 54, 205]
print(pattern)
for s in range()
print(pattern)

for l in range(0, len(pattern)):
    flip_list(pattern[l], currentPositionOut)
    currentPositionOut = (currentPositionOut + pattern[l] + skipSize) % len(a)
    skipSize += 1

print(str(a[0] * a[1]))
