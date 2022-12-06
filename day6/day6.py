#Read input
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
    file.close()

#Part 1
markerCheck = ''
result = 0
for line in input:
    for index in range(len(line)):
        markerCheck = line[index:index+4]
        markerFound = True
        for i, letter in enumerate(markerCheck):
            if letter in markerCheck[i+1:]:
                markerFound = False
        if markerFound == True:
            result = index+4
            break

print(result)

#Part 2
markerCheck = ''
result = 0
for line in input:
    for index in range(len(line)):
        markerCheck = line[index:index+14]
        markerFound = True
        for i, letter in enumerate(markerCheck):
            if letter in markerCheck[i+1:]:
                markerFound = False
        if markerFound == True:
            result = index+14
            break

print(result)