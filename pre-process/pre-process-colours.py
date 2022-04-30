dataset = open('colour-names', 'r')

colours = []

for line in dataset.readlines():
    line = line.replace(' -', '-')
    colour = line.split('-')[0]
    if len(colour.split(' ')) > 1:
        continue
    if not colour.isalpha():
        continue
    colours.append(colour)

f = open('colour', 'w')
for colour in colours:
    f.write(colour + '\n')
f.close()

