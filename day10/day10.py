#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

#Part 1
x = 1
cycle = 1
cycles = [20, 60, 100, 140, 180, 220]
result = 0
for line in input:
    instruction = line.split(' ')
    
    if cycle in cycles:
        result += cycle*x

    if len(instruction) == 2:
        cycle += 1
        if cycle in cycles:
            result += cycle*x
        cycle += 1
        x += int(instruction[1])
    else:
        cycle += 1

print(result)

#Part 2

#Count cycles
cycles = 0
for line in input:
    instruction = line.split(' ')

    if instruction[0] == 'noop':
        cycles += 1
    else:
        cycles += 2

#Run cycles
instructionIndex = 0
readyForInstruction = True
x = 1
screen = ''
sprite = []
for cycle in range(1, cycles+1):
    sprite = [x-1, x, x+1]

    if (cycle-1) % 40 in sprite:
        screen += '#'

    else:
        screen += '.'


    if cycle % 40 == 0:
        screen += '\n'

    if readyForInstruction:
        instruction = input[instructionIndex].split(' ')

        if instruction[0] == 'addx':
            amount = int(instruction[1])
            readyForInstruction = False
        else:
            instructionIndex += 1
    else:
        x += amount
        readyForInstruction = True
        instructionIndex += 1
    
print(screen)