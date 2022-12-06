#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

#Part 1
totalScore = 0
for line in input:
    #Rock == 1, Paper == 2, Scissors == 3
    values = {'A': 1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
    me = values[line[2]]
    opponent = values[line[0]]

    if me == opponent+1 or (opponent == 3 and me == 1):
        totalScore += 6
    elif me == opponent:
        totalScore += 3

    if me == 1:
        totalScore += 1
    elif me == 2:
        totalScore += 2
    elif me == 3:
        totalScore += 3

print(totalScore)

#Part 2
totalScore = 0
for line in input:
    outcome = line[2]
    #Rock == 1, Paper == 2, Scissors == 3
    values = {'A': 1, 'B':2, 'C':3}
    opponent = values[line[0]]
    
    if outcome == 'X':
        if opponent == 1:
            me = 3
        else:
            me = opponent-1
    elif outcome == 'Y':
        me = opponent
        totalScore += 3
    elif outcome == 'Z':
        if opponent == 3:
            me = 1
        else:
            me = opponent+1
        totalScore += 6

    if me == 1:
        totalScore += 1
    elif me == 2:
        totalScore += 2
    elif me == 3:
        totalScore += 3

print(totalScore)