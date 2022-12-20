#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

#OBS! RIKTIGT ÄCKLIG KOD; SNÄLLA FIXA TILL DEN

#Part 1
visibleTrees = len(input)*2+len(input[0])*2-4

for i, line in enumerate(input):
    if i != 0 and i != len(input)-1:
        row = line
        row = [int(x) for x in row]

        for j, tree in enumerate(row[1:-1]):
            col = []
            for line in input:
                col.append(line[j+1])
            col = [int(x) for x in col]
            visible = 4

            for left in row[0:j+1]:
                if left >= tree:
                    visible -= 1
                    break
            for right in row[j+2:]:
                if right >= tree:
                    visible -= 1
                    break
            for up in col[0:i]:
                if up >= tree:
                    visible -= 1
                    break
            for down in col[i+1:]:
                if down >= tree:
                    visible -= 1
                    break
            if visible != 0:
                visibleTrees += 1

print(visibleTrees)

#Part 2
visibleTrees = len(input)*2+len(input[0])*2-4
scenicScores = []

gridLeft = []
gridRight = []
for i, line in enumerate(input):
    row = line
    row = [int(x) for x in row]
    leftViews = []
    rightViews = []
    for j, tree in enumerate(row):
        col = []
        for line in input:
            col.append(line[j])
        col = [int(x) for x in col]
        visible = 4

        rowLeft = row[0:j]
        rowRight = row[j+1:]
        leftView = j
        rightView = len(rowRight)

        if not rowLeft:
            leftView = 0
        else:
            for leftIndex, left in enumerate(rowLeft[::-1]):
                if left >= tree:
                    leftView = leftIndex+1
                    break
        #print('leftView', leftView)
        leftViews.append(leftView)
        if not rowRight:
            rightView = 0
        else:
            for rightIndex, right in enumerate(rowRight):
                if right >= tree:
                    rightView = rightIndex+1
                    break
        print('rightView', rightView)
        rightViews.append(rightView)
    gridLeft.append(leftViews)
    gridRight.append(rightViews)

#Build col
grid = []
for line in input:
    col.append(line[j])
col = [int(x) for x in col]

gridUp = [ [] for _ in range(len(input)) ]
for i in range(len(input)):
    colUp = []
    #upViews = []
    for j in range(len(input[0])):
        tree = int(input[j][i])
        upView = j 
        if not colUp:
            upView = 0
        else:
            for upIndex, up in enumerate(colUp[::-1]):
                if up >= tree:
                    upView = upIndex+1
                    break
        #print('upView', upView)
        gridUp[j].append(upView)
        colUp.append(tree)
    #gridUp.append(upViews)

gridDown = [ [] for _ in range(len(input)) ]
for i in range(len(input)):
    colDown = []
    #downViews = []
    for j in range(len(input[0]))[::-1]:
        tree = int(input[j][i])
        downView = len(colDown)
        if not colDown:
            downView = 0
        else:
            for downIndex, down in enumerate(colDown[::-1]):
                if down >= tree:
                    downView = downIndex+1
                    break
        #print('downView', downView)
        gridDown[j].append(downView)
        colDown.append(tree)
    #gridDown.append(downViews[::-1])

for i in range(len(input)):
    for j in range(len(input[0])):
        scenicScores.append(gridLeft[i][j]*gridRight[i][j]*gridUp[i][j]*gridDown[i][j])

print(max(scenicScores))