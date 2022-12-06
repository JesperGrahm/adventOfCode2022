#Alternative Read
stackInput, moves = open('input.txt').read().split('\n\n')

#Part 1
numberOfStacks = int(stackInput.split('\n')[-1][-2])
stacks = {}
for i in range(numberOfStacks):
    stacks[str(i+1)] = []

for line in stackInput.split('\n')[:-1]:
    crates = line[1::4]
    for index, crate in enumerate(crates):
        if crate != ' ':
            stacks[str(index+1)].append(crate)

for stack in stacks:
    stacks[stack].reverse()

for move in moves.split('\n'):
    splitMove = move.split(' ')
    amount = int(splitMove[1])
    fromStack = splitMove[3]
    toStack = splitMove[5]
    moveCrates = []

    for i in range(amount):
        moveCrates.append(stacks[fromStack].pop())

    stacks[toStack] += moveCrates

result = ''
for stack in stacks:
    if stacks[stack]:
        result += stacks[stack].pop()

print(result)

#Part 2
numberOfStacks = int(stackInput.split('\n')[-1][-2])
stacks = {}
for i in range(numberOfStacks):
    stacks[str(i+1)] = []

for line in stackInput.split('\n')[:-1]:
    crates = line[1::4]
    for index, crate in enumerate(crates):
        if crate != ' ':
            stacks[str(index+1)].append(crate)

for stack in stacks:
    stacks[stack].reverse()

for move in moves.split('\n'):
    splitMove = move.split(' ')
    amount = int(splitMove[1])
    fromStack = splitMove[3]
    toStack = splitMove[5]
    moveCrates = []

    for i in range(amount):
        moveCrates.append(stacks[fromStack].pop())

    if moveCrates:
        moveCrates.reverse()
    stacks[toStack] += moveCrates

result = ''
for stack in stacks:
    if stacks[stack]:
        result += stacks[stack].pop()

print(result)