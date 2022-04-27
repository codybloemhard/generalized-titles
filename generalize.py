import sys

if len(sys.argv) < 2:
    print('No file argument given for the rules')
    exit()

rules = []

file = open(sys.argv[1], "r")
for line in file:
    if len(line) == 0:
        continue
    if line[0].isspace():
        continue
    words = line.split(' ')
    rule = []
    for word in words:
        if len(word) == 0:
            continue
        word = word.replace('\n', '')
        if word[0] == '/':
            rule.append((True, word))
        else:
            rule.append((False, word))
    if len(rule) > 0:
        rules.append(rule)

print(rules)
