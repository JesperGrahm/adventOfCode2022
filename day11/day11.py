#Alternative Read
monkeyData = open('input.txt').read().split('\n\n')

#Part 1
monkeys = {}
for monkey in monkeyData:
    lines = monkey.split('\n')
    id = lines[0][7]
    items = [int(item) for item in lines[1][17:].split(', ')]
    operation = lines[2][23:].split(' ')
    test = int(lines[3][21:])
    ifTrue = int(lines[4][29])
    ifFalse = int(lines[5][30])
    
    monkeys[id] = {
        'items': items,
        'operation': operation,
        'test': test,
        'ifTrue': ifTrue,
        'ifFalse': ifFalse,
        'inspections': 0
    }

#Real monkey business
for round in range(20):
    monkeysCopy = monkeys.copy()
    for monkey in monkeys:
        for itemWorry in monkeys[monkey]['items']:
            monkeys[monkey]['inspections'] += 1
            newItemWorry = 0
            if monkeys[monkey]['operation'][0] == '*':
                if monkeys[monkey]['operation'][1] == 'old':
                    newItemWorry = itemWorry * itemWorry
                else:
                    newItemWorry = itemWorry * int(monkeys[monkey]['operation'][1])
            else:
                newItemWorry = itemWorry + int(monkeys[monkey]['operation'][1])
            newestItemWorry = int(newItemWorry/3)
            if newestItemWorry % monkeys[monkey]['test'] == 0:
                monkeys[str(monkeys[monkey]['ifTrue'])]['items'].append(newestItemWorry)
            else:
                monkeys[str(monkeys[monkey]['ifFalse'])]['items'].append(newestItemWorry)
            monkeys[monkey]['items'] = monkeys[monkey]['items'][:-1]

#Calculating monkey business
inspections = []
for monkey in monkeys:
    inspections.append(monkeys[monkey]['inspections'])
inspections.sort()
inspections = inspections[-2:]

print(inspections[0]*inspections[1])

#Part 2
monkeys = {}
for monkey in monkeyData:
    lines = monkey.split('\n')
    id = lines[0][7]
    items = [int(item) for item in lines[1][17:].split(', ')]
    operation = lines[2][23:].split(' ')
    test = int(lines[3][21:])
    ifTrue = int(lines[4][29])
    ifFalse = int(lines[5][30])
    
    monkeys[id] = {
        'items': items,
        'operation': operation,
        'test': test,
        'ifTrue': ifTrue,
        'ifFalse': ifFalse,
        'inspections': 0
    }

#Real monkey business
for round in range(10000):
    monkeysCopy = monkeys.copy()
    for monkey in monkeys:
        for itemWorry in monkeys[monkey]['items']:
            monkeys[monkey]['inspections'] += 1
            newItemWorry = 0
            if monkeys[monkey]['operation'][0] == '*':
                if monkeys[monkey]['operation'][1] == 'old':
                    newItemWorry = itemWorry * itemWorry
                else:
                    newItemWorry = itemWorry * int(monkeys[monkey]['operation'][1])
            else:
                newItemWorry = itemWorry + int(monkeys[monkey]['operation'][1])
            if newItemWorry % monkeys[monkey]['test'] == 0:
                newestItemWorry = monkeys[monkey]['test']
                monkeys[str(monkeys[monkey]['ifTrue'])]['items'].append(newestItemWorry)
            else:
                monkeys[str(monkeys[monkey]['ifFalse'])]['items'].append(newItemWorry)
            monkeys[monkey]['items'] = monkeys[monkey]['items'][:-1]

#Calculating monkey business
inspections = []
for monkey in monkeys:
    inspections.append(monkeys[monkey]['inspections'])
inspections.sort()
inspections = inspections[-2:]

print(inspections[0]*inspections[1])
print(monkeys)