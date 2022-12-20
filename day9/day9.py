#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

def headInRange(tail):
    if head['x'] not in range(tail['x']-1, tail['x']+2) or head['y'] not in range(tail['y']-1, tail['y']+2):
        return False
    else:
        return True

def newTailPosition(tail):
    if head['x'] == tail['x'] or head['y'] == tail['y']:
        for i in range(4):
            if i == 0:
                x = 0
                y = 1
            elif i == 1:
                x = 0
                y = -1
            elif i == 2:
                x = -1
                y = 0
            elif i == 3:
                x = 1
                y = 0
            tempTail = {'x': tail['x']+x, 'y': tail['y']+y}
            if headInRange(tempTail):
                if tempTail not in visitedPositions:
                    visitedPositions.append(tempTail)
                return tempTail

    for x in range(-1, 2, 2):
        for y in range(-1, 2, 2):
            tempTail = {'x': tail['x']+x, 'y': tail['y']+y}
            if headInRange(tempTail):
                if tempTail not in visitedPositions:
                    visitedPositions.append(tempTail)
                return tempTail

def knotInRange(leaderKnot, followerKnot):
    if (leaderKnot['x'] not in range(followerKnot['x']-1, followerKnot['x']+2) 
        or leaderKnot['y'] not in range(followerKnot['y']-1, followerKnot['y']+2)):
        return False
    else:
        return True

def newKnotPosition(leaderKnot, followerKnot, isTail=False):
    #Check far diagonals
    for x in range(-2, 3, 4):
        for y in range(-2, 3, 4):
            if leaderKnot['x'] == followerKnot['x']+x and leaderKnot['y'] == followerKnot['y']+y:
                tempKnot = {'x': followerKnot['x']+int(x/2), 'y': followerKnot['y']+int(y/2)}
                print('leader', leaderKnot, 'temp', tempKnot)
                if knotInRange(leaderKnot, tempKnot):
                    if tempKnot not in visitedPositions and isTail:
                        if tempKnot == {'x': 1001, 'y': 1000}:
                            print('wrong', leaderKnot, followerKnot)    
                        visitedPositions.append(tempKnot)
                    return tempKnot
    if isTail:
        print('tail', followerKnot)
    #Check straight directions
    if leaderKnot['x'] == followerKnot['x'] or leaderKnot['y'] == followerKnot['y']:
        for i in range(4):
            if i == 0:
                x = 0
                y = 1
            elif i == 1:
                x = 0
                y = -1
            elif i == 2:
                x = -1
                y = 0
            elif i == 3:
                x = 1
                y = 0
            tempKnot = {'x': followerKnot['x']+x, 'y': followerKnot['y']+y}
            if knotInRange(leaderKnot, tempKnot):
                if tempKnot not in visitedPositions and isTail:
                    visitedPositions.append(tempKnot)
                    if tempKnot == {'x': 1001, 'y': 1000}:
                        print('wrong', leaderKnot, followerKnot)
                return tempKnot

    #Check rest
    for x in range(-1, 2, 2):
        for y in range(-1, 2, 2):
            tempKnot = {'x': followerKnot['x']+x, 'y': followerKnot['y']+y}
            if knotInRange(leaderKnot, tempKnot):
                if tempKnot not in visitedPositions and isTail:
                    visitedPositions.append(tempKnot)
                    if tempKnot == {'x': 1001, 'y': 1000}:
                        print('wrong', leaderKnot, followerKnot)
                return tempKnot

#Part 1
head = {'x': 1000, 'y': 1000}
tail = {'x': 1000, 'y': 1000}
visitedPositions = [{'x': 1000, 'y': 1000}]

for line in input:
    direction, distance = line.split(' ')
    distance = int(distance)

    for i in range(distance):
        if direction == 'U':
            head['y'] += 1
        elif direction == 'D':
            head['y'] -= 1
        elif direction == 'L':
            head['x'] -= 1
        elif direction == 'R':
            head['x'] += 1

        if not headInRange(tail):
            tail = newTailPosition(tail)

print(len(visitedPositions))

#Part 2
knots = {}
for i in range(10):
    knots[i] = {'x': 1000, 'y': 1000}
visitedPositions = [{'x': 1000, 'y': 1000}]

for line in input:
    direction, distance = line.split(' ')
    distance = int(distance)

    for i in range(distance):
        if direction == 'U':
            knots[0]['y'] += 1
        elif direction == 'D':
            knots[0]['y'] -= 1
        elif direction == 'L':
            knots[0]['x'] -= 1
        elif direction == 'R':
            knots[0]['x'] += 1

        for knotIndex in range(9):
            leaderKnot = knots[knotIndex]
            followerKnot = knots[knotIndex+1]
            if not knotInRange(leaderKnot, followerKnot):
                if followerKnot == knots[9]:
                    knots[knotIndex+1] = newKnotPosition(leaderKnot, followerKnot, True)
                else:
                    knots[knotIndex+1] = newKnotPosition(leaderKnot, followerKnot)
        
        
        print(knots)

#visitedPositions = [visitedPositions[0]] + visitedPositions[2:]
print(visitedPositions)
print(len(visitedPositions))