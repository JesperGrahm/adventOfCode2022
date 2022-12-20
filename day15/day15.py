import re
import numpy as np

#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

sensors = []
beacons = []
maxX = float('-inf')
minX = float('inf')
maxY = float('-inf')
minY = float('inf')
for line in input:
    coords = re.findall(rf'=([-]?[\d]*)', line)

    if max(int(coords[0]), int(coords[2])) > maxX:
        maxX = max(int(coords[0]), int(coords[2]))
    if min(int(coords[0]), int(coords[2])) < minX:
        minX = min(int(coords[0]), int(coords[2]))
    if max(int(coords[1]), int(coords[3])) > maxY:
        maxY = max(int(coords[1]), int(coords[3]))
    if min(int(coords[1]), int(coords[3])) < minY:
        minY = min(int(coords[1]), int(coords[3]))

    sensors.append([int(coords[0]), int(coords[1])])
    beacons.append([int(coords[2]), int(coords[3])])

rows = {}
#print(np.array([2,3]))
for i, sensor in enumerate(sensors):
    x = sensor[0]
    y = sensor[1]
    lenToBeacon = abs(beacons[i][0]-x) + abs(beacons[i][1]-y)

    # dipp = {}
    # for opp in range(10000000):
    #     if opp not in dipp:
    #         dipp[opp] = '1'
    #     if opp % 10000 == 0:
    #         print(opp)
    # print(lenToBeacon)
    
    #Calculate and store sensor coverage
    #if i == 6:
    for i in range(lenToBeacon):
        #print(i)
        firstKey = y-lenToBeacon+i
        secondKey = y+lenToBeacon-i
        if firstKey in rows:
            rows[firstKey].append([x-i, x+i])
        else:
            rows[firstKey] = [[x-i, x+i]]
        if secondKey in rows:
            rows[secondKey].append([x-i, x+i])
        else:
            rows[secondKey] = [[x-i, x+i]]
    if y in rows:
        rows[y].append([x-lenToBeacon, x+lenToBeacon])
    else:
        rows[y] = [[x-lenToBeacon, x+lenToBeacon]]
    print('new sensor')
    

noBeacon = set()
for span in rows[2000000]:
    for x in range(span[0], span[1]+1):
        noBeacon.add(x)
for beacon in beacons:
    if beacon[1] == 2000000 and beacon[0] in noBeacon:
        noBeacon.remove(beacon[0])
#print(noBeacon)
print(len(noBeacon))
#print(maxX, minX, maxY, minY)