import string

#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

#Part 1
priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)
prioritySum = 0

for line in input:
    compartMentSize = int(len(line)/2)
    firstHalf = line[0:compartMentSize]
    secondHalf = line[compartMentSize:]
    sharedLetter = ''

    for letter in firstHalf:
        if letter in secondHalf:
            prioritySum += priorities.index(letter)+1
            break

print(prioritySum)

#Part 2
priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)
prioritySum = 0
group = []

for line in input:
    if len(group) != 2:
        group.append(line)
    else:
        group.append(line)
        for letter in group[0]:
            if letter in group[1] and letter in group[2]:
                prioritySum += priorities.index(letter)+1
                break
        group = []

print(prioritySum)

