data = 265149
i = 1
sizeSquare = 0
difference = 0
cornerDisparity = 0
midpointCorner = 0
levelsFromCenter = 0
answer = 0
while data > i**2:
    i += 1

if i % 2 == 0:
    sizeSquare = i + 1
else:
    sizeSquare = i

levelsFromCenter = int((sizeSquare - 1) / 2)
difference = (sizeSquare ** 2) - data
while cornerDisparity * 2 - 1 != sizeSquare:
    cornerDisparity += 1
midpointCorner = 2 ** cornerDisparity
if (data == sizeSquare ** 2) or (data == (sizeSquare ** 2) - midpointCorner) or (data == (sizeSquare ** 2) - midpointCorner - 2 * levelsFromCenter) or (data == (sizeSquare ** 2) - midpointCorner + 2 * levelsFromCenter):
    answer = 2 * levelsFromCenter
elif (data == sizeSquare ** 2 - levelsFromCenter) or (data == (sizeSquare ** 2) - midpointCorner - levelsFromCenter) or (data == (sizeSquare ** 2) - midpointCorner - 3 * levelsFromCenter) or (data == (sizeSquare ** 2) - midpointCorner + levelsFromCenter):
    answer = levelsFromCenter
else:
    list1 = [abs((sizeSquare ** 2 - levelsFromCenter) - data), abs(((sizeSquare ** 2) - midpointCorner - levelsFromCenter) - data), abs(((sizeSquare ** 2) - midpointCorner - 3 * levelsFromCenter) - data), abs(((sizeSquare ** 2) - midpointCorner + levelsFromCenter) - data)]
    xDistance = min(list1)
    answer = levelsFromCenter + xDistance
print(answer)

