#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

#Part 1
total = 0
for line in input:
    pairs = line.split(',')
    firstStartEnd = pairs[0].split('-')
    secondStartEnd = pairs[1].split('-')
    firstElf = [*range(int(firstStartEnd[0]), int(firstStartEnd[1])+1, 1)]
    secondElf = [*range(int(secondStartEnd[0]), int(secondStartEnd[1])+1, 1)]

    firstCheck = all(number in firstElf for number in secondElf)
    secondCheck = all(number in secondElf for number in firstElf)

    if firstCheck or secondCheck:
        total += 1

print(total)

#Part 2
total = 0
for line in input:
    pairs = line.split(',')
    firstStartEnd = pairs[0].split('-')
    secondStartEnd = pairs[1].split('-')
    firstElf = [*range(int(firstStartEnd[0]), int(firstStartEnd[1])+1, 1)]
    secondElf = [*range(int(secondStartEnd[0]), int(secondStartEnd[1])+1, 1)]

    for number in firstElf:
        if number in secondElf:
            total += 1
            break

print(total)