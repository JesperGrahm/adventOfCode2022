import string

#Read input
with open('input.txt') as file:
    input = [[letter for letter in line.rstrip()] for line in file]
    file.close()

heights = ['S'] + list(string.ascii_lowercase) + ['E']

#Part 1
#Build adjacent and get starting coordinates
adjacentMatrix = [[[] for _ in range(len(input[0]))] for _ in range(len(input))]
for i in range(len(adjacentMatrix)):
    for j in range(len(adjacentMatrix[0])):
        if i != 0:
            adjacentMatrix[i][j].append((i-1, j))
        if j != 0:
            adjacentMatrix[i][j].append((i, j-1))
        if i != len(input)-1:
            adjacentMatrix[i][j].append((i+1, j))
        if j != len(input[0])-1:
            adjacentMatrix[i][j].append((i, j+1))

        if input[i][j] == 'S':
            startingCoords = (i, j)

def findPath(start, goal):
    stack = [(start, [start])]
    visited = set(start)
    while stack:
        (coords, path) = stack.pop(0)
        value = input[coords[0]][coords[1]]
        if value == goal:
            return path
        if coords not in visited:
            visited.add(coords)
            for adjacent in adjacentMatrix[coords[0]][coords[1]]:
                adjacentValue = input[adjacent[0]][adjacent[1]]
                if (heights.index(adjacentValue)-1 == heights.index(value) or
                    heights.index(adjacentValue) <= heights.index(value)):
                    stack.append((adjacent, path + [adjacent]))
                
path = findPath((startingCoords), 'E')
print(len(path)-1)

# output = input.copy()
# for i in range(len(output)):
#         for j in range(len(output[0])):
#             if (i, j) in path:
#                 output[i][j] = '-'
# with open('output.txt', 'w') as file:
#     for line in output:
#         file.writelines(line)
#         file.write('\n')
#     file.close()

#Part 2
#Build adjacent and get starting coordinates
startingCoords = []
adjacentMatrix = [[[] for _ in range(len(input[0]))] for _ in range(len(input))]
for i in range(len(adjacentMatrix)):
    for j in range(len(adjacentMatrix[0])):
        if i != 0:
            adjacentMatrix[i][j].append((i-1, j))
        if j != 0:
            adjacentMatrix[i][j].append((i, j-1))
        if i != len(input)-1:
            adjacentMatrix[i][j].append((i+1, j))
        if j != len(input[0])-1:
            adjacentMatrix[i][j].append((i, j+1))

        if input[i][j] in ['S', 'a']:
            startingCoords.append((i, j))

def findPath(start, goal):
    stack = [(start, [start])]
    visited = set(start)
    while stack:
        (coords, path) = stack.pop(0)
        value = input[coords[0]][coords[1]]
        if value == goal:
            return path
        if coords not in visited:
            visited.add(coords)
            for adjacent in adjacentMatrix[coords[0]][coords[1]]:
                adjacentValue = input[adjacent[0]][adjacent[1]]
                if (heights.index(adjacentValue)-1 == heights.index(value) or
                    heights.index(adjacentValue) <= heights.index(value)):
                    stack.append((adjacent, path + [adjacent]))
                
trails = []
for coords in startingCoords:
    thisPath = findPath(coords, 'E')
    if thisPath:
        trails.append(len(thisPath)-1)

print(min(trails))