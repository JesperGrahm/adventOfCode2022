import numpy as np

#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

#Part 1
#Build rocks
rocks = []
maxY = 0
for line in input:
    points = line.split(' -> ')
    for i in range(len(points)-1):
        firstX, firstY = [int(coord) for coord in points[i].split(',')]
        secondX, secondY = [int(coord) for coord in points[i+1].split(',')]
        #Set maxY
        if firstY > maxY:
            maxY = firstY
        if secondY > maxY:
            maxY = secondY
        
        #Build lines
        if firstX < secondX:
            for x in range(firstX, secondX+1):
                if [x, firstY] not in rocks:
                    rocks.append([x, firstY])
        elif firstX > secondX:
            for x in range(firstX, secondX-1, -1):
                if [x, firstY] not in rocks:
                    rocks.append([x, firstY])
        elif firstY < secondY:
            for y in range(firstY, secondY+1):
                if [firstX, y] not in rocks:
                    rocks.append([firstX, y])
        elif firstY > secondY:
            for y in range(firstY, secondY-1, -1):
                if [firstX, y] not in rocks:
                    rocks.append([firstX, y])

sand = []
oblivion = False
stoppedSand = 0
while not oblivion:
    sandX = 500
    sandY = 0

    while True:
        #Stop sand if it's falling in oblivion
        if sandY > maxY:
            oblivion = True
            break

        if [sandX, sandY+1] not in rocks + sand:
            sandY += 1
            continue
        elif [sandX, sandY+1] in rocks + sand and [sandX-1, sandY+1] not in rocks + sand:
            sandX -= 1
            sandY += 1
            continue
        elif [sandX, sandY+1] in rocks + sand and [sandX+1, sandY+1] not in rocks + sand:
            sandX += 1
            sandY += 1
            continue
        elif [sandX, sandY+1] in rocks + sand:
            sand.append([sandX, sandY])
            stoppedSand += 1
            break

print(stoppedSand)

#Part 2, takes about 20 sec
#Build rocks
map = np.chararray([1000,1000])
map[:] = '.'
map[500][0] = '+'
maxY = 0
for line in input:
    points = line.split(' -> ')
    for i in range(len(points)-1):
        firstX, firstY = [int(coord) for coord in points[i].split(',')]
        secondX, secondY = [int(coord) for coord in points[i+1].split(',')]
        #Set maxY
        if firstY > maxY:
            maxY = firstY
        if secondY > maxY:
            maxY = secondY
        
        #Build lines
        if firstX < secondX:
            for x in range(firstX, secondX+1):
                map[x][firstY] = '#'
        elif firstX > secondX:
            for x in range(firstX, secondX-1, -1):
                map[x][firstY] = '#'
        elif firstY < secondY:
            for y in range(firstY, secondY+1):
                map[firstX][y] = '#'
        elif firstY > secondY:
            for y in range(firstY, secondY-1, -1):
                map[firstX][y] = '#'

#Add bottom layer
for x in range(0, 1000):
    map[x][maxY+2] = '#'

sand = []
stoppedSand = 0

while [500, 0] not in sand:
    sandX = 500
    sandY = 0

    while True:
        if map[sandX][sandY+1] not in [b'#', b'O']:
            sandY += 1
            continue
        elif map[sandX][sandY+1] in [b'#', b'O'] and map[sandX-1][sandY+1] not in [b'#', b'O']:
            sandX -= 1
            sandY += 1
            continue
        elif map[sandX][sandY+1] in [b'#', b'O'] and map[sandX+1][sandY+1] not in [b'#', b'O']:
            sandX += 1
            sandY += 1
            continue
        elif map[sandX][sandY+1] in [b'#', b'O']:
            sand.append([sandX, sandY])
            map[sandX][sandY] = 'O'
            stoppedSand += 1
            break

print(stoppedSand)