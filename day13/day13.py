import functools

#Alternative Read
input = open('input.txt').read().split('\n\n')

#Part 1
def compare(first, second):
    #Result is set to either -1 or 1 to make the function work as a comparator for part 2
    #-1 means the pair is in correct order, 1 means it is not in correct order
    result = None
    if len(first) < len(second):
        result = -1
    elif len(first) > len(second):
        result = 1
    for i in range(min(len(first), len(second))):
        #Both ints
        if isinstance(first[i], int) and isinstance(second[i], int):
            if first[i] < second[i]:
                result = -1
                return result
            elif first[i] > second[i]:
                result = 1
                return result
        #Both lists
        if isinstance(first[i], list) and isinstance(second[i], list):
            recursion = compare(first[i], second[i])
            if recursion != None:
                result = recursion
                return result
        #First int, second list
        if isinstance(first[i], int) and isinstance(second[i], list):
            recursion = compare([first[i]], second[i])
            if recursion != None:
                result = recursion
                return result
        #First list, second int
        if isinstance(first[i], list) and isinstance(second[i], int):
            recursion = compare(first[i], [second[i]])
            if recursion != None:
                result = recursion
                return result
    return result

rightPairs = []

for i, x in enumerate(input):
    pair = x.split('\n')
    first = eval(pair[0])
    second = eval(pair[1])
    
    result = compare(first, second)
    if result == -1:
        rightPairs.append(i+1)

print(sum(rightPairs))

#Part 2
input = [eval(i) for i in open('input.txt').read().split('\n') if i != ''] + [[[2]]] + [[[6]]]
sortedList = sorted(input, key=functools.cmp_to_key(compare))
dividers = [0, 0]

for index, item in enumerate(sortedList):
    if item == [[2]]:
        dividers[0] = index+1
    elif item == [[6]]:
        dividers[1] = index+1

print(dividers[0] * dividers[1])