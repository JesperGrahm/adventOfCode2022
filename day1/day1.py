#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

#Part 1
elfCalories = 0
maxCalories = 0
for line in input:
    if line != '':
        elfCalories += int(line)
    else:
        if elfCalories > maxCalories:
            maxCalories = elfCalories
        elfCalories = 0

print(maxCalories)

#Part 2
elfCalories = 0
allElfCalories = []
for line in input:
    if line != '':
        elfCalories += int(line)
    else:
        allElfCalories.append(int(elfCalories))
        elfCalories = 0
maxCalories.sort()

elf = 0
total = 0
for elf in allElfCalories[-3:]:
    total += elf

print(total)