import re
with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]
index = set()
beaconXs = set()

for line in lines:
    x = list(map(int, re.findall("(?<=x=)[-]?[0-9]*", line)))
    y = list(map(int, re.findall("(?<=y=)[-]?[0-9]*", line)))
    sensorX, sensorY, beaconX, beaconY = x[0], y[0], x[1], y[1]
    if beaconY == 2000000:
        beaconXs.add(beaconX)
    distanceX, distanceY = abs(sensorX - beaconX), abs(sensorY - beaconY)
    distance = distanceX + distanceY
    differenceY = abs(sensorY - 2000000)
    for i in range(sensorX - distance + differenceY, sensorX + distance - differenceY + 1):
        index.add(i)

index = index - beaconXs

print(len(index))