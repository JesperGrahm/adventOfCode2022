from anytree import Node, RenderTree, PreOrderIter, LevelOrderGroupIter
import sys
#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

#Part 1
root = Node('root', size=0)
currentDirectory = root

for line in input:
    splitLine = line.split(' ')

    if splitLine[0] == '$':
        if splitLine[1] == 'cd':
            if splitLine[2] == '..':
                currentDirectory = currentDirectory.parent
            else:
                for child in currentDirectory.children:
                    if child.name == splitLine[2]:
                        currentDirectory = child
    elif splitLine[0] == 'dir':
        node = Node(splitLine[1], parent=currentDirectory, size=0)
    elif splitLine[0].isnumeric():
        node = Node(splitLine[1], parent=currentDirectory, size=splitLine[0])

levels = [[node for node in children] for children in LevelOrderGroupIter(root)]

for nodes in levels[::-1]:
    for node in nodes:
        if node.parent != None:
            node.parent.size += int(node.size)

directorySum = sum([int(node.size) for node in PreOrderIter(root) if int(node.size) <= 100000 and node.children ])

print(directorySum)

#Part 2
root = Node('root', size=0)
currentDirectory = root

for line in input:
    splitLine = line.split(' ')

    if splitLine[0] == '$':
        if splitLine[1] == 'cd':
            if splitLine[2] == '..':
                currentDirectory = currentDirectory.parent
            else:
                for child in currentDirectory.children:
                    if child.name == splitLine[2]:
                        currentDirectory = child
    elif splitLine[0] == 'dir':
        node = Node(splitLine[1], parent=currentDirectory, size=0)
    elif splitLine[0].isnumeric():
        node = Node(splitLine[1], parent=currentDirectory, size=splitLine[0])

levels = [[node for node in children] for children in LevelOrderGroupIter(root)]

for nodes in levels[::-1]:
    for node in nodes:
        if node.parent != None:
            node.parent.size += int(node.size)

smallestDirectory = sys.maxsize
for node in PreOrderIter(root):
    size = int(node.size)
    if node.children and size > abs(root.size-40000000) and size < smallestDirectory:
        smallestDirectory = size

print(smallestDirectory)